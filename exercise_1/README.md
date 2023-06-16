# Exercise 1

1. Wystartuj instancję ghosta ([docs](https://hub.docker.com/_/ghost)):

   ```bash
   $ sudo docker run -d --name my-ghost -e NODE_ENV=development -e url=http://localhost:3001 -p 3001:2368 ghost
   $ sudo docker ps
   ```

   Open in browser: http://127.0.0.1:3001

2. W osobnym terminalu wyświetlmy logi:

   ```bash
   $ sudo docker logs my-ghost -f
   ```

3. Czas, na testy. Zacznijmy, klasycznie, z Siege ([homepage](https://www.joedog.org/siege-home/)):

   ```bash
   $ siege -t15s -c2 –header='X-USER-AGENT:android_4.4.4' 127.0.0.1:3001
   ```

   ```bash
   $ siege -t15s -c100 –header='X-USER-AGENT:android_4.4.4' 127.0.0.1:3001
   ```

   ```bash
   $ siege -t15s -c255 127.0.0.1:3001
   ```

   Co się zmieniło w logach ghosta?

   Przejrzyj:

   ```bash
   $ siege --help
   ```

   Zauważ, możesz do siege przekazać listę plików z URLami.

4. Czas na bardziej złożone narzędzie - [locust.io](https://locust.io/). Przejrzyj: `locustfile.py`. Zapoznaj się z dokumentacją: [docs.locust.io/en/stable/writing-a-locustfile.html](https://docs.locust.io/en/stable/writing-a-locustfile.html).

5. Teraz czas na jego uruchomienie:

   ```bash
   # najpierw czas na zainstalowanie wymaganych bibliotek
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install locust

   # czas zacząć test
   $ locust -f locustfile.py
   ```

   Otwórz: http://127.0.0.1:8089, konfiguracja:

   - Number of users: 50
   - Spawn Rate: 10
   - Host: http://127.0.0.1:3001

6. Czas wyłączyć nasz kontener z blogiem:

   ```bash
   $ sudo docker stop my-ghost
   $ sudo docker rm my-ghost
   # powinieneś zobaczyć pustą listę
   $ sudo docker ps
   ```
