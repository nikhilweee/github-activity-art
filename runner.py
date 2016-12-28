import dates
import text
import os
import datetime

repo_dir_name = 'activity-art-repo'

def commit_datetimes():
    date_matrix = dates.dates()
    text_matrix = text.decision()

    date_flattened = [
        date for date_submatrix in date_matrix for date in date_submatrix]
    text_flattened = [
        char for text_submatrix in text_matrix for char in text_submatrix]

    commit_dates = [date_flattened[x]
                    for x in range(7 * 51) if text_flattened[x] == '#']
    commit_datetimes = [datetime.datetime.combine(
        date, datetime.time(14)) for date in commit_dates]

    return(commit_datetimes)


def init_repo():
    os.mkdir(repo_dir_name)
    os.chdir(repo_dir_name)
    os.system('git init')


def make_change(timestamp):
    filename = timestamp.strftime('%Y-%m-%d-%H-%M-%S')
    with open(filename, 'w') as f:
        f.write(filename)
    print('created file {}'.format(filename))


def commit(datetime):
    author = 'Author Name <authorname@email.com>'
    date = datetime.isoformat()
    os.system('git add --all')
    os.system('git commit --message {} --author "{}" --date {}'
              .format('commit-message', author, date))

if __name__ == '__main__':
    commit_datetimes = commit_datetimes()
    init_repo()
    for timestamp in commit_datetimes:
        make_change(timestamp)
        commit(timestamp)
