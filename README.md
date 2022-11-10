# Instructions to run Backend 
## Docker
1. Start local database
2. Create .env file with values 
```
# Docker 
DB_HOSTNAME=host.docker.internal
DB_USERNAME=root
DB_PASSWORD=''
DB_NAME=test_spm_db
```
2. Run respective sql script located in `./tests/sql`
3. Run Command  ``` docker build -t backend .  ```
4. Run Command `docker run -p 5000:5000 backend` 
