import datetime
from haystack import indexes
from .models import Chemistry
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ChemistryIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    compoundformula = indexes.CharField(model_attr='molecularformula')
    cid = indexes.CharField(model_attr='cid',null=True)

    def get_model(self):
        return Chemistry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        logger.info("%s has been searched",self.get_model())
        return self.get_model().objects.all()
        # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())