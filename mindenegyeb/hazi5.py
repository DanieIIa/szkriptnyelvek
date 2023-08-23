#!/usr/bin/env python3

def main():
    starters = [
        [ 'Andre Iguodala', 4, 3, 7, 8, " " ],
        [ 'Klay Thompson', 5, 0, 21, 3, "THIRD"],
        [ 'Stephen Curry', 5, 8, 36, 1, "FIRST"],
        [ 'Draymon Green', 9, 4, 11, 6, "SECOND"],
        [ 'Andrew Bogut', 3, 0, 2, 2, " "],
    ]
    row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} | {asd:2d} | {asr:<7s} |".format

    for p in starters:
        print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3], asd=p[4], asr=p[5]))
    
    s1 = "cats"
    s2 = "dogs"
    s3 = " %s and %s living together" % (s1, s2)
    s4 = " {} and {} living together ".format(s1, s2)
    print(s3)
    print(s4)


if __name__ == "__main__":
    main()