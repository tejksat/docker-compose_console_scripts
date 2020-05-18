# Sample Docker Compose project with an entry point in *setup.py*

1. Given that `wfh` script is declared in `console_scripts` in *setup.py*:
   ```
   ...
   
   setup(
       ...
       entry_points={
           'console_scripts': ['wfh=wfh.command_line:main']
       }
   )
   ```

2. *setup.py* could be installed during building the Docker image:
   ```
   ...
   RUN python setup.py develop
   ...
   ```

3. This command could be used then in *docker-compose.yml*:
   ```
   version: '3'
   services:
     app:
       build: .
       command: wfh
   ```
