SMALL_TALK = 'Small Talk'
BUSINESS = 'Business'
COUNTER_CULTURE = 'Counter Culture'
LABOR = 'Labor'
OCCULT = 'Occult'
PHILOSOPHY = 'Philosophy'
PSYCHEDELIA = 'Psychedelia'
TOM_FOOLERY = 'Tom Foolery'
POLITICS = 'Politics'
SPORTS = 'Sports'
NATURE = 'Nature'
FASHION = 'Fashion'
TECH = 'Tech'
GASTRONOMY = 'Gastronomy'
HEALTH = 'Health'

INTERESTS = {
    SMALL_TALK, BUSINESS, COUNTER_CULTURE, LABOR, OCCULT, PHILOSOPHY, PSYCHEDELIA,
    TOM_FOOLERY, POLITICS, SPORTS, NATURE, FASHION, TECH, GASTRONOMY, HEALTH
}


# These interests are 'positively co-orelated', i.e., someone interested in business is interested in politics
STRONG_AGAINST = {
    SMALL_TALK: {SMALL_TALK},
    BUSINESS: {BUSINESS, POLITICS, TECH},
    COUNTER_CULTURE: {COUNTER_CULTURE, PSYCHEDELIA, PHILOSOPHY},
    LABOR: {LABOR, TOM_FOOLERY},
    OCCULT: {OCCULT, PSYCHEDELIA},
    PHILOSOPHY: {PHILOSOPHY, PSYCHEDELIA, COUNTER_CULTURE, TECH},
    PSYCHEDELIA: {PSYCHEDELIA, NATURE, FASHION, COUNTER_CULTURE},
    TOM_FOOLERY: {TOM_FOOLERY, LABOR},
    POLITICS: {POLITICS, SMALL_TALK, BUSINESS},
    SPORTS: {SPORTS, HEALTH},
    NATURE: {NATURE, HEALTH},
    FASHION: {FASHION, BUSINESS, COUNTER_CULTURE},
    TECH: {BUSINESS, PSYCHEDELIA, PHILOSOPHY},
    GASTRONOMY: {GASTRONOMY, OCCULT},
    HEALTH: {HEALTH, GASTRONOMY, SPORTS}
}

# These interests are negatively co-orelated, someone into Tech is not into Sports or Fashion
WEAK_AGAINST = {
    SMALL_TALK: {HEALTH, TECH, POLITICS, PSYCHEDELIA, PHILOSOPHY, OCCULT},
    BUSINESS: {NATURE, TOM_FOOLERY, PSYCHEDELIA, PHILOSOPHY, OCCULT, COUNTER_CULTURE},
    COUNTER_CULTURE: {BUSINESS, SMALL_TALK},
    LABOR: {COUNTER_CULTURE},
    OCCULT: {HEALTH, SMALL_TALK, BUSINESS},
    PHILOSOPHY: {SMALL_TALK},
    PSYCHEDELIA: {BUSINESS, SMALL_TALK},
    TOM_FOOLERY: {BUSINESS},
    POLITICS: {PSYCHEDELIA, NATURE},
    SPORTS: {TECH},
    NATURE: {BUSINESS},
    FASHION: {TECH},
    TECH: {SPORTS, FASHION},
    GASTRONOMY: {},
    HEALTH: {}
}

def rate_interests():
    """
    Run an analysis of each interest to produce a measurement of its overall 'effectiveness' according to the
    following formula

    interest_rating =
        |offensive advantages| + |defensive advantaged| - |offensive disadvantages| - |defensive disadvantages|
            |                              |
          number of times        size of weak against     number of times this        size of strong against
          this appears in                                 appears in other
          other strong againsts                           weak againsts


    Returns:
        dict of [str: int]: numeric rating for each interest

    """
    ratings = dict.fromkeys(INTERESTS, 0)
    for i in INTERESTS:
        ratings[i] -= len(STRONG_AGAINST[i])
        ratings[i] += len(WEAK_AGAINST[i])
        for o in STRONG_AGAINST[i]:
            ratings[o] += 1
        for o in WEAK_AGAINST[i]:
            ratings[o] -= 1

    return ratings


if __name__ == '__main__':
    from pprint import pprint
    print("Here are the power rankin's")
    ratings = rate_interests()
    for i in sorted(list(ratings.keys())):
        print("{:<16}  {:>2}".format(i.capitalize() + ":", ratings[i]))