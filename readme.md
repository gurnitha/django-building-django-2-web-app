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
	│   .gitignore                       
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