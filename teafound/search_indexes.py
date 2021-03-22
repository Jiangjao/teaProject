import datetime
from haystack import indexes
from .models import CodeImages


class CodeImagesIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    compoundformula = indexes.CharField(model_attr='compoundformula')
    cid = indexes.CharField(model_attr='cid',null=True)

    def get_model(self):
        return CodeImages

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
        # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())