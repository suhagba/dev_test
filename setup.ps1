function create-venv {
    & python '-m' 'venv' 'env'
    & '.\env\Scripts\activate'
    }
     
    function activate-venv {
    & '.\env\Scripts\activate'
    }

    function install-dep {
        & pip install -r requirements.txt
        }

    create-venv
    activate-venv
    install-dep