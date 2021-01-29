## Benchmarking and Timeouts

1. Jeśli będziesz potrzebowała w prosty sposób pomierzyć czas wykonania:

   ```
   python3 -m unittest test_running_time_simple.py
   ```

2. A co gdy nie chcemy, aby nas test skończył się w zadanym czasie?

   ```
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install pytest pytest-timeout

   # jeśli pytest -timeout=1 nie działa to:
   $ deactivate
   $ source .venv/bin/activate

   # zauważ marker w teście
   $ pytest test_with_timeout.py

   # tutaj podajemy timeout jako argument
   $ pytest -timeout=1 test_running_time_simple.py
   ```

3. Wyobrażmy sobie teraz mamy fragment kodu, który chcemy zrozumieć jak zachowa się dla danych:

   ```
   $ python with_timeit.py
   ```

4. Na co zwrócić uwagę, pisząc swój własny kod:

   - [timeouts w produkcji zawsze](https://requests.readthedocs.io/en/master/user/quickstart/#timeouts)
   -  Obsługa `429` - rate limiting serwera:

      ```python
      retry = 3
      while retry > 0:
          r = request.get(url, timeout=0.001, 
          	              headers={'Authorization': token})
          if response.status_code == 429:
              time.sleep(1)
              retry = retry - 1
      ```
