import os
import datetime
import git
from font import Font


def year_in_review():
    today = datetime.datetime.today()
    difference = datetime.timedelta(6 - today.weekday())
    coming_sunday = today + difference
    first_sunday = coming_sunday - datetime.timedelta(weeks=53)
    dates = [list() for x in range(7)]
    # list of sublists having dates by weekday
    for x in range(52 * 7):
        dates[x % 7].append(first_sunday + datetime.timedelta(x))
    return dates


def generate_stencil(text_to_render):
    # Be sure to place 'subway-ticker.ttf' (or any other ttf / otf font file)
    # in the working directory.
    font = Font('subway-ticker.ttf', 8, 10)
    text = repr(font.render_text(text_to_render, 52, 7))
    # text.split always adds an extra element, '\n'. Strip that off
    text_by_weekday = text.split('\n')[:-1]
    stencil = [list(x) for x in text_by_weekday]
    return text, stencil


def generate_commit_dates(stencil_matrix):
    date_matrix = year_in_review()

    date_flattened = [
        date for date_submatrix in date_matrix for date in date_submatrix]
    stencil_flattened = [
        char for text_submatrix in stencil_matrix for char in text_submatrix]
    commit_dates = [date_flattened[x]
                    for x in range(52 * 7) if stencil_flattened[x] == '#']
    return commit_dates


if __name__ == '__main__':
    while(True):
        text_to_render = input('Please enter text to render: ')
        try:
            generate_stencil(text_to_render)
        except IndexError:
            print('Sorry, that was too long. Please try again.')
        else:
            break
    text_to_render = text_to_render or 'nikhilweee'
    text, stencil_matrix = generate_stencil(text_to_render)
    print('\nThis is roughly how the activity graph would look like:\n')
    print(text)

    # get author info
    repo_dir_name = input('Please enter the directory name for the new repo: ')
    repo_dir_name = repo_dir_name or 'activity-art-repo'
    author_name = input('Please enter your name as on GitHub: ')
    author_name = author_name or 'Nikhil Verma'
    author_email = input('Please enter your email as on GitHub: ')
    author_email = author_email or 'nikhilweee@gmail.com'
    author = git.Actor(author_name, author_email)
    print('\nAll commits will be made by "{} <{}>"'.format(
        author_name, author_email))

    commit_dates = generate_commit_dates(stencil_matrix)

    # commits per day
    commits_per_day = input(
        'Enter the number of commits per day (blank for 1): ')
    commits_per_day = commits_per_day or 1
    commits_per_day = int(commits_per_day)
    print('\nCreating {:d} commits. Please be patient.'.format(
        len(commit_dates) * commits_per_day))

    repo = git.Repo.init(repo_dir_name)

    for date in commit_dates:
        for x in range(commits_per_day):
            timestamp = datetime.datetime.combine(date, datetime.time(14 + x))
            filename = timestamp.strftime('%Y-%m-%d-%H-%M-%S')
            filepath = os.path.join(repo_dir_name, filename)
            with open(filepath, 'w') as f:
                f.write(filename)
            repo.index.add([filename])
            repo.index.commit("commit for github-activity-art", author=author,
                              committer=author, author_date=timestamp.isoformat())

    push_url = input(
        '\nPlease create a new repository on GitHub. Enter its push url here: ')
    try:
        repo.remotes.origin.set_url(push_url)
    except:
        repo.create_remote('origin', push_url)
    repo.remotes.origin.push(refspec='refs/heads/master:refs/heads/master')
    print('\nYou should now be able to see this activity graph art on GitHub.',
          '\nCheers!')
