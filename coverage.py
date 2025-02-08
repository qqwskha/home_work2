import os
import subprocess


def run_coverage():
    """
    Запускает тесты и генерирует отчет о покрытии тестами.
    """
    print("Запуск тестов и сбор покрытия...")

    # Команда для запуска тестов и сбора данных о покрытии
    subprocess.run(["coverage", "run", "-m", "pytest", "tests/"])

    # Генерация отчета в консоль
    print("\nОтчет о покрытии тестами:")
    subprocess.run(["coverage", "report", "-m"])

    # Генерация HTML-отчета
    print("\nГенерация HTML-отчета...")
    subprocess.run(["coverage", "html"])

    # Открытие HTML-отчета в браузере (для Windows)
    html_report_path = os.path.join(os.getcwd(), "htmlcov", "index.html")
    if os.name == "nt":  # Для Windows
        os.startfile(html_report_path)
    else:  # Для macOS/Linux
        subprocess.run(["open", html_report_path])


if __name__ == "__main__":
    run_coverage()