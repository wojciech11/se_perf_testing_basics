## Benchmarking and Timeouts

1. Jeśli będziesz potrzebowała w prosty sposób pomierzyć czas wykonania. Przeanalizuj `test_running_time_simple.py`, a następnie wykonaj:

   ```bash
   python3 -m unittest test_running_time_simple.py
   ```

2. A co gdy chcemy, aby nas test skończył się w zadanym czasie? A może mamy kod, który może się zablokować? Z pomocą przychodzi biblioteka [pytest-timeout](https://pypi.org/project/pytest-timeout/).

   ```bash
   $ python3 -m venv .venv
   $ source .venv/bin/activate

   # zainstalujmy
   # wymaganą biblioteke
   $ pip install pytest pytest-timeout

   # sprawdź czy plugin dziala:
   $ pytest --timeout=1

   # jeśli nie to zdeaktywuj i aktywuj venv:
   $ deactivate
   $ source .venv/bin/activate
   ```

   Przanalizuj plik `test_measure_time_with_timeout.py`, a następnie wykonaj:

   ```bash
   # zauważ marker w teście
   $ pytest test_measure_time_with_timeout.py
   ```

   Teraz możemy ustalić również timeout dla każdego testu jednostkowego:

   ```bash
   # tutaj podajemy timeout jako argument
   $ pytest --timeout=1 test_running_time_simple.py
   ```

3. Wyobrażmy sobie teraz mamy fragment kodu, który chcemy zrozumieć jak zachowa się dla danych:

   ```bash
   $ python with_timeit.py
   ```

4. Na co zwrócić uwagę, pisząc swój własny kod:

   - [timeouts w produkcji zawsze](https://docs.python-requests.org/en/master/user/advanced/#timeouts)
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

   - więcej na [github.com/wojciech11/se_http_api_testing_quickstart](https://github.com/wojciech11/se_http_api_testing_quickstart).
