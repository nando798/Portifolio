from dataclasses import dataclass
from pathlib import Path


@dataclass
class Category:
    name: str
    planned: float
    real: float

    @property
    def diference(self) -> float:
        return self.real - self.planned


class MonthBudget:
    def __init__(self):
        self.categories: list[Category] = []

    def total_add(self, name: str, planned: float, real: float) -> None:
        self.categories.append(Category(name, planned, real))

    def total_planned(self) -> float:
        return sum(c.planned for c in self.categories)

    def total_real(self) -> float:
        return sum(c.real for c in self.categories)

    def total_diference(self) -> float:
        return sum(c.diference for c in self.categories)

    def resume(self) -> str:
        lines = []
        lines.append(f"{"Category":0} {"Planned":>9} {"Real":>19} {"Diference":>24}")
        lines.append("-" * 70)
        for c in self.categories:
            lines.append(
                f"{c.name:10} "
                f"Planned: R$ {c.planned:10.2f} "
                f"Real: R$ {c.real:10.2f} "
                f"Diference: R$ {c.diference:10.2f}"
            )
        return "\n".join(lines)

    def save_excel(self, directory: Path) -> None:
        try:
            import pandas as pd
        except ImportError:
            print("Pandas is not installed. Please install it to use this feature.")
            return

        df = pd.DataFrame(
            [
                {
                    "Caregory": c.name,
                    "Planned": c.planned,
                    "Real": c.real,
                    "Diference": c.diference,
                }
                for c in self.categories
            ]
        )
        df.to_excel(directory, index=False)
        print(f"Planned saved in {directory}")


if __name__ == "__main__":
    budget = MonthBudget()

# Pergunta qula o salario mesal.

income = _read_number("Enter your monthly income: R$ ")
budget.set_income(income)
print(f"Sálario mensal definido: R$ {budget.income: 2f}\n")

dados = [
    ("Food", 1500.00, 1600.00),
    ("Water", 50.00, 60.00),
    ("Energy", 250.00, 230.00),
    ("Internet", 120.00, 120.00),
    ("Credit Card", 1500.00, 1400.00),
]
for name, p, i in dados:
    budget.total_add(name, p, i)
print(budget.resume())

# print(f"DEBUG: added category {name}. with planned {len(budget.categories)}")
# print("---Adição Concluída---")
# opcional: salvar
# budget.save_excel(Path(__file__).parent / "budget.xlsx")
