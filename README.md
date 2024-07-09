# These are the SYC Ops Scripts/Tools for Servers Operations

To start using these scripts, you need to clone this repository, got to directory cstation and run the `pip install -e .` script.


## Prepare Odoo Codebase


### For Local Development Server

We can use the following script to prepare the Odoo codebase for local development server:

!!! note
    Prepare Odoo 16.0 for local development

    ```bash
    $ cd cstation
    $ cstation odoo local 16.0
    ```

    The Odoo 16.0 codebase will be cloned and prepared for local development at _/opt/PW/Odoo.16.0
    

### For Production Server

We can use the following script to prepare the Odoo codebase for production server:

!!! note
    Prepare Odoo 16.0 for production server

    ```bash
    $ cd cstation
    $ cstation odoo server 16.0
    ```

    The Odoo 16.0 codebase will be cloned and prepared for production server.