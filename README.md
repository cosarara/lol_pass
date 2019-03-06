# League of Legends auto login linux thing

I used to use <https://github.com/nicoco007/LoL-Auto-Login>
but then it stopped working on wine so whatever.

Depending on the resolution you'll need to change
the template screenshot (`pass.png`).

Change the `subprocess.Popen(["league_nopass"])`
to some command that runs league on your machine.

Write your pass in `pass.txt`:

    $ echo hunter2 > pass.txt

Install [poetry](https://github.com/sdispater/poetry).

Install the dependencies:

    $ poetry install

Run:

    $ poetry run python lol_pass.py

License is X11, read the file named `LICENSE`.
