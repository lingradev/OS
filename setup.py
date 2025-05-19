from setuptools import setup, find_packages

setup(
    name="lingra",
    version="1.0.0",
    packages=find_packages(where="backend"),
    package_dir={"": "backend"},
    include_package_data=True,
    install_requires=open("backend/requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "lingra-train=scripts.train_model:main",
            "lingra-server=scripts.run_server:main",
        ],
    },
    author="Lingra Dev Team",
    description="Lingra OS – Autonomous LLM system",
    license="MIT",
    keywords=["llm", "ai", "crypto", "fastapi", "transformers"],
    zip_safe=False,
) 