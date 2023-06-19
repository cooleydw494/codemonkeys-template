import argparse

from monkeycore.base_entitiies.automation_class import Automation
from monkeycore.utils.monk.theme.theme_functions import print_t
from modules.tasks.process_file import process_file
from modules.tasks.summarize_context import summarize_context_file


class Default(Automation):
    required_config_keys = ['WORK_PATH', 'MAIN_PROMPT', 'OUTPUT_EXT']

    def __init__(self, monk_args: argparse.Namespace):
        super().__init__(monk_args)

    def main(self):

        m = self.monkey_config

        context_file_summary = summarize_context_file(m, allow_unsummarized=True)

        self.fpm.write_files_to_process()

        while True:
            selected_file = self.fpm.select_and_remove_file()

            if selected_file is None:
                print_t("All files have been processed.", 'done')
                break

            process_file(selected_file, context_file_summary, m)
