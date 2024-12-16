from django.http import HttpResponse, HttpResponseRedirect
from .models import FinderObject
from django.db.models import Sum, Count, F
from django.db.utils import IntegrityError
from hurry.filesize import size
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from .forms import UploadFolderForm
from .services.finder import Finder
from .services.research_router import ResearchRouter
# Create your views here.


def index(request) -> HttpResponse:
    if request.method == "POST":
        form = UploadFolderForm(request.POST)
        if form.is_valid():
            HttpResponseRedirect("/fileanalyzer/")
    else:
        form = UploadFolderForm()

    indexing_files_total_size: str = (
        size(FinderObject.objects.all().aggregate(total_size=Sum("size"))["total_size"])
        if FinderObject.objects.all().count() != 0
        else "No data"
    )
    template = loader.get_template("fileanalyzer/index.html")
    context = {"indexing_files_total_size": indexing_files_total_size, "form": form}
    return HttpResponse(template.render(context, request))


def extensions(request) -> HttpResponse:
    total_files = FinderObject.objects.all().filter(type="File").count()
    files_count_by_extension = (
        FinderObject.objects.all()
        .filter(type="File")
        .values("extension")
        .annotate(
            count=Count("id"),
        )
        .order_by("-count")
    )
    template = loader.get_template("fileanalyzer/dashboard.html")
    context = {
        "files_count_by_extension": files_count_by_extension,
        "total_files": total_files,
        "chart_title": "Stats by extensions",
    }
    return HttpResponse(template.render(context, request))


def size_top(request) -> HttpResponse:
    top_files_by_size = (
        FinderObject.objects.all().filter(type="File").order_by("-size")[:10]
    )

    for file in top_files_by_size:
        file.size = size(file.size)

    template = loader.get_template("fileanalyzer/top_by_size.html")
    context = {"top_files_by_size": top_files_by_size}

    return HttpResponse(template.render(context, request))


def images_top(request) -> HttpResponse:
    top_images_by_res = (
        FinderObject.objects.all()
        .filter(type="File", file_type="Image")
        .annotate(area=F("width") * F("height"))
        .order_by("-area")[:10]
    )

    template = loader.get_template("fileanalyzer/top_by_res.html")
    context = {"top_images_by_res": top_images_by_res}

    return HttpResponse(template.render(context, request))


def docs_top(request) -> HttpResponse:
    top_docs_by_pages_count = (
        FinderObject.objects.all()
        .filter(type="File", file_type="Text", pages_count__isnull=False)
        .order_by("-pages_count")[:10]
    )

    template = loader.get_template("fileanalyzer/top_by_pages.html")
    context = {"top_docs_by_pages_count": top_docs_by_pages_count}

    return HttpResponse(template.render(context, request))


def info(request, file_id) -> HttpResponse:
    return HttpResponse(f"Здесь будет информация о файле {file_id}")


def analyze_folder(request) -> HttpResponse:
    finder = Finder()
    research_router = ResearchRouter()
    for finder_object in finder.get_results(request.POST["folder_path"]):
        try:
            FinderObject.objects.get(path=finder_object["path"])
        except IntegrityError:
            continue
        except ObjectDoesNotExist:
            if finder_object["type"] == "File":
                file_type, metadata = research_router.get_file_info(
                    finder_object["path"]
                )
                finder_object["file_type"] = file_type
                if file_type == "Image" and metadata:
                    finder_object["width"] = metadata["common_info"]["width"]
                    finder_object["height"] = metadata["common_info"]["height"]
                if file_type == "Text":
                    if metadata:
                        finder_object["pages_count"] = metadata["pages_count"]

            FinderObject.objects.create(**finder_object)

    return HttpResponseRedirect("/fileanalyzer/")
