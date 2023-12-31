from codemonkeys.utils.monk.theme_functions import print_t, print_table


def main():
    print_t("List Processes Help", "important")
    print_t("This script provides an overview of all ongoing Monk processes, their process IDs (PIDs),"
            "and commands to kill the respective processes.")

    print_t("monk list-processes.py", "input")

    usage_examples_table = {
        "headers": [
            "PID",
            "Command",
            "Kill Command"
        ],
        "show_headers": True,
        "rows": [
            [
                "1234",
                "monk add-monkey",
                "kill 1234"
            ],
            [
                "4567",
                "monk -a Default",
                "kill 4567"
            ],
        ]
    }

    print_table(usage_examples_table, "Usage")
