from pandas import read_excel


class Config:
    """CONFIG DATA CLASS"""

    def __init__(self, config_path: str) -> None:
        """INIT METHOD"""
        self._config_path = config_path
        self.readParametersFromConfig()
        self.read_projects_to_process()

    def readParametersFromConfig(self):
        """GET INFORMATION FROM CONFIG FILE"""
        self._configDf = read_excel(self._config_path, "Config")
        configDict = self._configDf.to_dict("split")
        for rowData in configDict["data"]:
            setattr(self, rowData[0], rowData[1])

    def read_projects_to_process(self):
        """GET INFORMATION FROM COMPANIES IN CONFIG"""
        self.projects_to_process_df = read_excel(self._config_path, "Executar")

    def saveExecutionConfig(self):
        """SAVE CONFIG"""
        self._configDf.to_csv(rf"{self._working_dir}\Config.csv")


if __name__ == "__main__":
    config = Config(r".\Input\Config.xlsx")
    #  print("")
