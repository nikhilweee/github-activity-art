# Activity Art for GitHub

Create pixel art on the GitHub contributions graph

![nikhilweee](http://i.imgur.com/o0eEjOE.png)

### Acknowledgements
[Dan Bader](https://twitter.com/dbader_org)'s [blog post](https://dbader.org/blog/monochrome-font-rendering-with-freetype-and-python) helped me create stencil matrix from TTF fonts. Thank you Dan!

### First steps
1. Create and activate a `python3` virtual environment (optional). `python2` might work fine as well.

```sh
virtualenv venv --python=python3
source venv/bin/activate

```
2. Install the dependencies from `requirements.txt`

```sh
pip install -r requirements.txt
```

### Usage
Just run `main.py` as a normal python script and answer the questions along the way!

```sh
python main.py
```

```
Please enter text to render: nikhilweee

This is roughly how the activity graph would look like:

.......#..#....#.....#..##..........................
..##......#....#.........#..#....#..##...##...##....
.#..#.##..#..#.###..##...#..#.#..#.#..#.#..#.#..#...
.#..#..#..#.#..#..#..#...#..#.#..#.#..#.#..#.#..#...
.#..#..#..##...#..#..#...#..#.#..#.####.####.####...
.#..#..#..#.#..#..#..#...#..#.#..#.#....#....#......
.#..#...#.#..#.#..#...#...#..#.#....##...##...##....

Please enter the directory name for the new repo: activity-art-repo
Please enter your name as on GitHub: Nikhil Verma
Please enter your email as on GitHub: nikhilweee@gmail.com

All commits will be made by "Nikhil Verma <nikhilweee@gmail.com>"
Enter the number of commits per day (blank for 1): 1

Creating 114 commits. Please be patient.

Please create a new repository on GitHub. Enter its push url here: https://github.com/nikhilweee/activity-art-repo.git
Username for 'https://github.com': nikhilweee
Password for 'https://nikhilweee@github.com':

You should now be able to see this activity graph art on GitHub.
Cheers!
```
