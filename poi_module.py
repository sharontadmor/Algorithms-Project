import pandas as pd
import requests


URL = 'https://gisn.tel-aviv.gov.il/arcgis/rest/services/IView2/MapServer/572/query?where=1%3D1&outFields=*&f=json'
POI = 'features'
POI_ATTRIBUTES = 'attributes'
POI_GEO = 'geometry'
POI_NAME = 'attributes.shem_angli'
X = 'geometry.x'
Y = 'geometry.y'
NO_ERROR = 200


def get_response():
    """
    Returns:
        Response : response for request of data from an API.
    """
    return requests.get(URL)


def get_data():
    """
    processes data retreived from an API.
    Returns:
        DataFrame: a pandas data frame containing the names of poi (points of interest) and their datum-points.
    """
    response = get_response()
    if not response:  # evaluate to True if the status code was not between 200 and 400, and False otherwise.
        return
    poi = response.json()[POI]  # get a list of only the points of interest.
    df = pd.json_normalize(poi)  # add data to DataFrame.
    df = df[[POI_NAME, X, Y]].sort_values(POI_NAME, ignore_index=True)  # keep only relevant data.
    df = df.rename(columns={POI_NAME : "name", X : "x", Y : "y"}) # rename columns.
    return df


# print(get_data())