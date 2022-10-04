from datetime import datetime
from os import mkdir
from os import walk
from os.path import join

from openpyxl import load_workbook
from pandas import DataFrame

from Snippets.configRead import Config


class Initializer(Config):
    """INIT CLASS"""

    def __init__(self, configPath: str) -> None:
        """INIT METHOD"""
        self._config_path = configPath
        super().__init__(self._config_path)
        self.check_if_project_folder_exists()

    def check_if_project_folder_exists(self):
        """DIRECTORY CHECK METHOD"""
        *args, directories, files = next(walk(self.output_folder))
        self.contract_folder_list = []
        for _index, row_content in self.projects_to_process_df.iterrows():
            contract_folder = join(self.output_folder, row_content.CONTRATO)
            self.contract_folder_list.append([contract_folder, row_content.CONTRATO, row_content.SEÇÃO])
            if row_content.CONTRATO not in directories:
                mkdir(contract_folder)

    def create_working_dir(self):
        """CREATE REAL TIME FOLDER"""
        now = datetime.now()
        output_folder_name = now.strftime("%Y%m%d%H%M%S")
        self._working_dir = join(self.contract_folder, output_folder_name)
        mkdir(self._working_dir)

    def create_empty_report(self, working_dir, sheet_name):
        """CREATE EXCEL REPORT FOR OUTPUT"""
        self.columns_report_splitted = self.columns_report.split(",")
        self._report_df = DataFrame(columns=self.columns_report_splitted)
        self._report_path = join(working_dir, "OutputReport.xlsx")
        self._report_df.to_excel(self._report_path, sheet_name, index=False)

    def write_to_report(self, new_row, sheet_name):
        """WRITE IN OUTPUT REPORT"""
        wb = load_workbook(self._report_path)
        ws = wb[sheet_name]
        ws.append(new_row)
        wb.save(self._report_path)
        wb.close()

    def get_files_in_folder(self, folder_to_process):
        """GET FILES IN A SPECIFIC FOLDER"""
        to_process_folder_path = join(self.input_folder, folder_to_process)
        *args, files = next(walk(to_process_folder_path))
        self._folder_files = [join(to_process_folder_path, file_name) for file_name in files]
        return self._folder_files

    def get_all_folders(self):
        """GET ALL FOLDER FROM A DIRECTORY"""
        path, input_directorys, files = next(walk(self.input_folder))
        files_to_process = []
        for input_directory in input_directorys:
            folder_files = self.get_files_in_folder(input_directory)
            for file_path in folder_files:
                files_to_process.append(file_path)

        return files_to_process

    def get_input_files(self):
        """GET FILES USED AS INPUT"""
        if self.to_process_folder == "ALL":
            self.files_to_process = self.get_all_folders()
        else:
            self.files_to_process = self.get_files_in_folder(self.to_process_folder)

        return self.files_to_process
