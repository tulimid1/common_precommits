# common_precommits
Precommits common to projects

1. Install pre-commit
| uv add pre-commit

2. Add .pre-commit-config.yaml file

3. Install git hook scripts 
| uv run pre-commit install

4. Install pre-push too
| uv run pre-commit install --hook-type pre-push

5. Check working
| uv run pre-commit run --all-files
