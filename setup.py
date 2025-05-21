from setuptools import setup, find_packages

# Load all required dependencies from requirements.txt
with open("backend/requirements.txt") as f:
    requirements = f.read().splitlines()

# Configure the Lingra OS Python package
setup(
    # Basic metadata
    name="lingra",
    version="1.0.0",
    author="Lingra Dev Team",
    description="Lingra OS – Autonomous LLM system",
    license="MIT",
    keywords=["llm", "ai", "crypto", "fastapi", "transformers"],

    # Package discovery
    packages=find_packages(where="backend"),      # Only scan inside /backend
    package_dir={"": "backend"},                  # Root package path is /backend
    include_package_data=True,                    # Include non-Python files (e.g. static, templates)

    # Dependencies
    install_requires=requirements,

    # CLI entry points
    entry_points={
        "console_scripts": [
            "lingra-train=scripts.train_model:main",   # Train command: lingra-train
            "lingra-server=scripts.run_server:main",   # Launch API server: lingra-server
        ],
    },

    # Packaging preferences
    zip_safe=False,  # Not safe to run from zipped .egg (uses file paths internally)
)
