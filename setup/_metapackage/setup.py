import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-agreement",
    description="Meta package for oca-agreement Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-agreement>=15.0dev,<15.1dev',
        'odoo-addon-agreement_legal>=15.0dev,<15.1dev',
        'odoo-addon-agreement_rebate>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
