from .baselib.building import TaxonomyData, BuildingBase
from .eu_cdn.building import Building as EuCDN
from .eu_cdl.building import Building as EuCDL
from .eu_cdm.building import Building as EuCDM
from .eu_cdh.building import Building as EuCDH
from .tr_pre75.building import Building as TrPre75
from .tr_7599.building import Building as Tr7599
from .tr_0018.building import Building as Tr0018
from .tr_post18.building import Building as TrPost18


def get_bdim(taxonomy: TaxonomyData) -> BuildingBase:
    """
    Returns a BDIM instance of the corresponding design class in taxonomy.

    Parameters
    ----------
    taxonomy : str
        Building taxonomy data.

    Returns
    -------
    BuildingBase
        A BDIM instance of the corresponding design class.
    """
    # Mapping from design_class attribute of taxonomy to each bdim class
    design_classes = {
        "eu_cdn": EuCDN,
        "eu_cdl": EuCDL,
        "eu_cdm": EuCDM,
        "eu_cdh": EuCDH,
        "tr_pre75": TrPre75,
        "tr_7599": Tr7599,
        "tr_0018": Tr0018,
        "tr_post18": TrPost18
    }
    # Get appropriate bdim class
    bdim = design_classes.get(taxonomy.design_class)
    # Check if the design_class is valid
    if bdim is None:
        raise ValueError(f"Invalid design class: {taxonomy.design_class}")
    # Instantiate and return the appropriate class
    return bdim(taxonomy)
