export FLASK_APP=manage.py
export FLASK_DEBUG=1
alias dbup='python manage.py db upgrade'
alias dbmg='python manage.py db migrate'
alias pjshell='python manage.py shell'