## Building Django 2.0 Web Applications

### 1. Basic setup: Created project with db connected

        new file:   .gitignore
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   readme.md

### 2. Created and registered app to project

	E:\workspace\django\building-django2-
	(venv3920) λ tree /f                 
	Folder PATH listing                  
	Volume serial number is 00000159 D810
	E:.                                  
	│   .gitignore      i                 
	│   manage.py                        
	│   readme.md                        
	│                                    
	├───app                              
	│   └───core                         
	│       │   admin.py                 
	│       │   apps.py                  
	│       │   models.py                
	│       │   tests.py                 
	│       │   views.py                 
	│       │   __init__.py              
	│       │                            
	│       └───migrations               
	│               __init__.py          
	│                                    
	└───config                           
	    │   settings.py                  
	    │   urls.py                      
	    │   wsgi.py                      
	    │   __init__.py                  
	    │                                
	    └───__pycache__                  
	            settings.cpython-39.pyc  
	            urls.cpython-39.pyc      
	            wsgi.cpython-39.pyc      
	            __init__.cpython-39.pyc         


### 3. Created amd registered Movie model 

        modified:   app/core/admin.py
        modified:   app/core/apps.py
        new file:   app/core/migrations/0001_initial.py
        modified:   app/core/models.py
        modified:   config/settings.py
        modified:   readme.md

### 4. Creating MovieList view

        modified:   app/core/views.py
        modified:   readme.md

### 5. Adding our first template d movie_list.html

        modified:   config/settings.py
        modified:   readme.md
        new file:   templates/core/movie_list.html

### 6. Routing requests to our view with URLConf

        new file:   app/core/urls.py
        modified:   config/urls.py
        modified:   readme.md


























































































































































