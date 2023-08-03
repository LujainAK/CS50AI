import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def mutation(mother, father, zero_gene, one_gene, two_genes, type):
    '''
    To Calcualte Mutation
        m for mutation and nm for not mutation
        type is the person's gene 
    '''
    
    m = PROBS["mutation"]
    nm = 1 - PROBS["mutation"]
    if type == 0:
        if mother in zero_gene and father in zero_gene:
            return nm * nm
        elif (mother in one_gene and father in zero_gene) or (mother in zero_gene and father in one_gene):
            return nm * 0.5
        elif (mother in zero_gene and father in two_genes) or (mother in two_genes and father in zero_gene):
            return nm * m
        elif mother in one_gene and father in one_gene:
            return 0.5 * 0.5
        elif (mother in one_gene and father in two_genes) or (mother in two_genes and father in one_gene):
            return 0.5 * m
        elif mother in two_genes and father in two_genes:
            return m * m
        
    elif type == 1:
        if (mother in zero_gene and father in zero_gene) or (mother in two_genes and father in two_genes):
            return m * nm + m * nm
        elif (mother in one_gene and father in zero_gene) or (mother in zero_gene and father in one_gene) or (mother in one_gene and father in two_genes) or (mother in two_genes and father in one_gene):
            return m * 0.5 + nm * 0.5
        elif (mother in zero_gene and father in two_genes) or (mother in two_genes and father in zero_gene):
            return nm * nm + m * m
        elif mother in one_gene and father in one_gene:
            return 0.5 * 0.5 + 0.5 * 0.5
        
    elif type == 2:
        if mother in zero_gene and father in zero_gene:
            return m * m
        elif (mother in one_gene and father in zero_gene) or (mother in zero_gene and father in one_gene):
            return m * 0.5
        elif (mother in zero_gene and father in two_genes) or (mother in two_genes and father in zero_gene):
            return m * nm
        elif mother in one_gene and father in one_gene:
            return 0.5 * 0.5
        elif (mother in one_gene and father in two_genes) or (mother in two_genes and father in one_gene):
            return 0.5 * nm
        elif mother in two_genes and father in two_genes:
            return nm * nm
    



def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    zero_gene = set()
    joints = []
    
    for i in people:
        if i not in one_gene and i not in two_genes:
            zero_gene.add(i)

    for i in zero_gene:
        mother = people[i]["mother"]
        father = people[i]["father"]
        if mother is None and father is None:
            p = PROBS["gene"][0]
        else:
            p = mutation(mother, father, zero_gene, one_gene, two_genes, 0)

        if i in have_trait:
            p *= PROBS["trait"][0][True]
        else:
            p *= PROBS["trait"][0][False]
        
        joints.append(p)

    for i in one_gene:
        mother = people[i]["mother"]
        father = people[i]["father"]
        if mother is None and father is None:
            p = PROBS["gene"][1]
        else:
            p = mutation(mother, father, zero_gene, one_gene, two_genes, 1)

        if i in have_trait:
            p *= PROBS["trait"][1][True]
        else:
            p *= PROBS["trait"][1][False]

        joints.append(p)

    for i in two_genes:
        mother = people[i]["mother"]
        father = people[i]["father"]
        if mother is None and father is None:
            p = PROBS["gene"][2]
        else:
            p = mutation(mother, father, zero_gene, one_gene, two_genes, 2)

        if i in have_trait:
            p *= PROBS["trait"][2][True]
        else:
            p *= PROBS["trait"][2][False]

        joints.append(p)

    result = 1
    for i in joints:
        result = result * i
    return result



def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p
        
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        oldT = probabilities[person]["trait"][True]
        oldF = probabilities[person]["trait"][False]
        ssum = oldT + oldF
        if ssum != 1:
            probabilities[person]["trait"][True] = oldT / ssum
            probabilities[person]["trait"][False] = oldF / ssum

        old0 = probabilities[person]["gene"][0]
        old1 = probabilities[person]["gene"][1]
        old2 = probabilities[person]["gene"][2]
        ssum = old0 + old1 + old2
        if ssum != 1:
            probabilities[person]["gene"][0] = old0 / ssum
            probabilities[person]["gene"][1] = old1 / ssum
            probabilities[person]["gene"][2] = old2 / ssum


if __name__ == "__main__":
    main()
