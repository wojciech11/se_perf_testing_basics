# Podstawy testowanie wydajności aplikacji

- [slajdy](slides/slides.pdf) ([md](slides/slides.md))

## Przygotowanie

W czasie ćwiczeń będziemy pracować na linuxie, rekomendujemy Ubuntu LTS w wersji [20.04.6](https://wiki.ubuntu.com/Releases).


Do ćwieczeń będzie nam porzebny docker, zainstaluj posługując się poniższymi komentami ([docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)):

```bash
# install necessary packages
$ sudo apt-get update
#
$ sudo apt-get install -y ca-certificates curl gnupg

# Add Docker’s official GPG key:
$ sudo install -m 0755 -d /etc/apt/keyrings

#
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
# Setting up the repository:
$ echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Install `docker-ce`:

```bash
#
$ sudo apt-get update
#
$ sudo apt-get install docker-ce docker-ce-cli
```

Check whether it works:

```bash
$ sudo docker run hello-world
```

## Materiały dodatkowe

- [Engineering You - Martin Thompson](https://www.youtube.com/watch?v=S4LzzuMTqjs)
