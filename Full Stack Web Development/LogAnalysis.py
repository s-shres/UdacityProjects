#!/usr/bin/python


import psycopg2


def main():
    db = psycopg2.connect('dbname=news')
    c = db.cursor()

    pop_3_art = """
    SELECT articleOverview.title, articleOverview.views
    FROM articleOverview
    ORDER BY articleOverview.views DESC LIMIT 3;
                """
    c.execute(pop_3_art)
    print('////////////////////////////////////////////////')
    print('The Three Most Popular Articles')
    for (title, view) in c.fetchall():
        print(' ' + title + '| Views:' + str(view))
    print('////////////////////////////////////////////////')

    pop_authors = """
                    SELECT articleOverview.name,
                    SUM(articleOverview.views)
                    AS authorTotViews
                    FROM articleOverview
                    GROUP BY articleOverview.name
                    ORDER BY authorTotViews DESC;
                   """
    c.execute(pop_authors)
    print('The Most Popular Authors:')
    for (name, view) in c.fetchall():
        print(' ' + name + '| Views:' + str(view))
    print('////////////////////////////////////////////////')

    errors = \
        """
        SELECT *
        FROM calcError
        WHERE calcError.rate > 1
        """
    c.execute(errors)
    print('The Following Days Had More than 1% of Request that Led to Errors')
    for (date, rate) in c.fetchall():
        print(' ' + str(date) + '| Error Rate: ' + str(round(rate,2)) + '%')
    print('////////////////////////////////////////////////')


if __name__ == '__main__':
    main()
