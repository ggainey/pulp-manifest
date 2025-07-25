from setuptools import setup, find_packages


setup(
    name="pulp_manifest",
    version="3.1.0",
    license="GPLv2+",
    packages=find_packages(),
    author="Pulp Team",
    author_email="pulp-list@redhat.com",
    description="Tool to generate a PULP_MANIFEST file for a given directory,"
    " so the directory can be recognized by Pulp.",
    extras_require={
        "s3": ["boto3==1.39.1"],
    },
    entry_points={
        "console_scripts": [
            "pulp-manifest = pulp_manifest.build_manifest:main",
        ]
    },
)
