from rich.console import Console
from rich.table import Table

def print_table(results):
    table = Table(title="Results")
    table.add_column("Case")
    table.add_column("Scorer")
    table.add_column("Result")

    for case_id, scorer_type, passed, detail in results:
        result = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
        table.add_row(case_id, scorer_type, result)

    Console().print(table)