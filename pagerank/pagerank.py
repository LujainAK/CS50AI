import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    tm = dict()
    tm = {key: 0 for key in corpus.keys()}

    if len(corpus[page]) != 0:
        for i in corpus[page]:
            tm[i] += damping_factor/len(corpus[page])

    for i in corpus:
        if len(corpus[page]) == 0:
            tm[i] += damping_factor/len(corpus)
        else: 
            for j in corpus[page]:
                tm[j] += damping_factor/len(corpus[page])
        tm[i] += (1-damping_factor)/len(corpus)

    return tm


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    PR = dict()
    PR = {key: 0 for key in corpus.keys()}
    randPage = random.choice(list(corpus))
    PR[randPage] += 1

    for i in range(n-1):
        tm = transition_model(corpus, randPage, damping_factor)
        randPage = random.choices(list(tm.keys()), weights = list(tm.values()), k = 1)[0]
        PR[randPage] += 1

    for i in PR:
        PR[i] = PR[i]/n

    return PR



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    PR = dict()
    PR = {key: float(1/N) for key in corpus.keys()}

    #stop = False
    while True:
        maxDiff = 0
        newPR = dict()
        for page in corpus:
            ssum = 0
            for link in corpus:
                if page in corpus[link]:
                    ssum += (PR[link] / len(corpus[link]))
            newPR[page] = ((1 - damping_factor ) / N) + damping_factor * ssum
            if abs(newPR[page] - PR[page]) > maxDiff:
                maxDiff = abs(newPR[page] - PR[page])

        if maxDiff < 0.001:
            break
        
        PR = newPR

    # Normalize PageRank values:
    totalPR = sum(PR.values())
    for page in PR:
        PR[page] = PR[page] / totalPR

    return PR


if __name__ == "__main__":
    main()
