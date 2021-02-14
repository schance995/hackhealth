# Yale COVID-19 Statistics AR
COVID-19 data visualizer for Yale University statistics using Unity and EchoAR. 
Our project is an extension of an EchoAR sample Unity project [here](https://github.com/echoARxyz/Unity-echoAR-demo-COVID19).

Check out our [Devpost](https://devpost.com/software/yale-covid-statistics-ar) for more information!


## Register
Don't have an API key? Make sure to register for FREE at [echoAR](https://console.echoar.xyz/#/auth/register).

## Setup
* Create a new Unity project.
* [Install the echoAR Unity SDK](https://docs.echoar.xyz/unity/installation).
* Open the sample scene under `echoAR/Examples/sample.unity`.
* [Set the API key](https://docs.echoar.xyz/unity/using-the-sdk) in the Inspector of the echoAR game object.
* [Add the 3D model](https://docs.echoar.xyz/quickstart/add-a-3d-model) from the [models](https://github.com/echoARxyz/Unity-echoAR-demo-COVID19/tree/master/models) folder to the console.
* [Add the metadata](https://docs.echoar.xyz/web-console/manage-pages/data-page/how-to-add-data#adding-metadata) listed in the [metadata.csv](https://github.com/echoARxyz/Unity-echoAR-demo-COVID19/blob/master/models/metadata.csv) file.
* Overwrite the existing _echoAR/CustomBehaviour.cs_ and _echoAR/RemoteTransformations.cs_ with the files in the _Unity_ subdirectory of the repo.
* Install Python dependencies:
    * numpy
    * beautifulsoup
    * requests
* Edit the Python script and substitute in your API key.
    * For production purposes, the API key should not be stored directly in the source code. But we didn't have time to do this.

## Run
Simply press the _Play_ button in Unity.
You can refresh the data in real time by running the Python script.

## Thanks
* To Women in Computer Science at Stony Brook University for hosting the hackathon.
* To EchoAR for providing their AR service.

## Copying
* Please read the license for information.
