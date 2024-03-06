# Generated from d://Code scripts//Principles of Programming Languages//PPL_AS2//assignment2//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,554,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,1,0,
        1,0,1,0,1,1,5,1,123,8,1,10,1,12,1,126,9,1,1,1,1,1,1,1,1,1,5,1,132,
        8,1,10,1,12,1,135,9,1,1,1,3,1,138,8,1,1,2,1,2,1,2,1,2,1,2,3,2,145,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,156,8,4,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,
        13,1,14,1,14,1,14,1,14,1,14,3,14,181,8,14,1,15,1,15,1,15,1,15,1,
        15,3,15,188,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,197,8,16,
        10,16,12,16,200,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,209,
        8,17,10,17,12,17,212,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,
        221,8,18,10,18,12,18,224,9,18,1,19,1,19,1,19,1,19,3,19,230,8,19,
        1,20,1,20,1,20,1,20,3,20,236,8,20,1,21,1,21,3,21,240,8,21,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,252,8,22,1,23,1,
        23,1,24,1,24,1,24,3,24,259,8,24,1,25,1,25,4,25,263,8,25,11,25,12,
        25,264,1,25,1,25,4,25,269,8,25,11,25,12,25,270,1,25,1,25,4,25,275,
        8,25,11,25,12,25,276,3,25,279,8,25,1,26,1,26,1,26,3,26,284,8,26,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,293,8,27,1,28,1,28,1,28,
        1,28,1,28,3,28,300,8,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,3,31,316,8,31,1,32,1,32,1,32,1,32,
        1,32,1,33,1,33,1,33,1,33,3,33,327,8,33,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,36,1,36,1,36,1,36,1,36,3,36,341,8,36,1,37,1,37,1,37,
        1,37,1,37,1,37,5,37,349,8,37,10,37,12,37,352,9,37,1,37,1,37,1,38,
        1,38,1,38,1,38,3,38,360,8,38,1,39,1,39,1,39,1,39,1,39,3,39,367,8,
        39,1,40,1,40,1,40,1,40,1,40,1,40,3,40,375,8,40,1,41,1,41,1,41,3,
        41,380,8,41,1,42,1,42,4,42,384,8,42,11,42,12,42,385,1,42,1,42,4,
        42,390,8,42,11,42,12,42,391,1,42,1,42,4,42,396,8,42,11,42,12,42,
        397,1,42,1,42,1,42,1,42,4,42,404,8,42,11,42,12,42,405,1,42,1,42,
        4,42,410,8,42,11,42,12,42,411,1,42,1,42,4,42,416,8,42,11,42,12,42,
        417,1,42,1,42,4,42,422,8,42,11,42,12,42,423,1,42,1,42,4,42,428,8,
        42,11,42,12,42,429,3,42,432,8,42,1,43,1,43,1,43,1,44,1,44,3,44,439,
        8,44,1,45,1,45,1,45,1,45,1,45,5,45,446,8,45,10,45,12,45,449,9,45,
        1,45,1,45,1,46,1,46,1,46,1,46,1,46,5,46,458,8,46,10,46,12,46,461,
        9,46,1,46,1,46,1,47,1,47,5,47,467,8,47,10,47,12,47,470,9,47,1,47,
        1,47,3,47,474,8,47,1,48,1,48,5,48,478,8,48,10,48,12,48,481,9,48,
        1,48,1,48,1,48,1,49,1,49,5,49,488,8,49,10,49,12,49,491,9,49,1,49,
        1,49,1,49,3,49,496,8,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,5,50,
        505,8,50,10,50,12,50,508,9,50,1,50,1,50,1,51,1,51,1,52,1,52,1,53,
        1,53,1,53,3,53,519,8,53,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,
        1,55,3,55,530,8,55,1,56,1,56,1,56,1,56,1,56,3,56,537,8,56,1,57,1,
        57,4,57,541,8,57,11,57,12,57,542,1,57,1,57,1,57,1,58,1,58,1,58,1,
        58,3,58,552,8,58,1,58,0,3,32,34,36,59,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        108,110,112,114,116,0,5,1,0,30,32,1,0,28,29,1,0,43,44,2,0,34,39,
        41,41,1,0,11,13,564,0,118,1,0,0,0,2,137,1,0,0,0,4,144,1,0,0,0,6,
        146,1,0,0,0,8,155,1,0,0,0,10,157,1,0,0,0,12,159,1,0,0,0,14,161,1,
        0,0,0,16,163,1,0,0,0,18,165,1,0,0,0,20,167,1,0,0,0,22,169,1,0,0,
        0,24,171,1,0,0,0,26,173,1,0,0,0,28,180,1,0,0,0,30,187,1,0,0,0,32,
        189,1,0,0,0,34,201,1,0,0,0,36,213,1,0,0,0,38,229,1,0,0,0,40,235,
        1,0,0,0,42,239,1,0,0,0,44,251,1,0,0,0,46,253,1,0,0,0,48,258,1,0,
        0,0,50,278,1,0,0,0,52,283,1,0,0,0,54,292,1,0,0,0,56,299,1,0,0,0,
        58,301,1,0,0,0,60,305,1,0,0,0,62,315,1,0,0,0,64,317,1,0,0,0,66,326,
        1,0,0,0,68,328,1,0,0,0,70,331,1,0,0,0,72,340,1,0,0,0,74,342,1,0,
        0,0,76,359,1,0,0,0,78,366,1,0,0,0,80,374,1,0,0,0,82,379,1,0,0,0,
        84,431,1,0,0,0,86,433,1,0,0,0,88,438,1,0,0,0,90,440,1,0,0,0,92,452,
        1,0,0,0,94,473,1,0,0,0,96,475,1,0,0,0,98,495,1,0,0,0,100,497,1,0,
        0,0,102,511,1,0,0,0,104,513,1,0,0,0,106,518,1,0,0,0,108,520,1,0,
        0,0,110,529,1,0,0,0,112,536,1,0,0,0,114,538,1,0,0,0,116,551,1,0,
        0,0,118,119,3,2,1,0,119,120,5,0,0,1,120,1,1,0,0,0,121,123,5,9,0,
        0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,
        0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,3,50,25,0,128,129,3,2,
        1,0,129,138,1,0,0,0,130,132,5,9,0,0,131,130,1,0,0,0,132,135,1,0,
        0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,
        0,0,136,138,3,50,25,0,137,124,1,0,0,0,137,133,1,0,0,0,138,3,1,0,
        0,0,139,140,5,45,0,0,140,145,3,6,3,0,141,142,3,108,54,0,142,143,
        3,6,3,0,143,145,1,0,0,0,144,139,1,0,0,0,144,141,1,0,0,0,145,5,1,
        0,0,0,146,147,5,6,0,0,147,148,3,8,4,0,148,149,5,7,0,0,149,7,1,0,
        0,0,150,151,3,26,13,0,151,152,5,8,0,0,152,153,3,8,4,0,153,156,1,
        0,0,0,154,156,3,26,13,0,155,150,1,0,0,0,155,154,1,0,0,0,156,9,1,
        0,0,0,157,158,3,4,2,0,158,11,1,0,0,0,159,160,5,29,0,0,160,13,1,0,
        0,0,161,162,5,42,0,0,162,15,1,0,0,0,163,164,7,0,0,0,164,17,1,0,0,
        0,165,166,7,1,0,0,166,19,1,0,0,0,167,168,7,2,0,0,168,21,1,0,0,0,
        169,170,7,3,0,0,170,23,1,0,0,0,171,172,5,40,0,0,172,25,1,0,0,0,173,
        174,3,28,14,0,174,27,1,0,0,0,175,176,3,30,15,0,176,177,3,24,12,0,
        177,178,3,30,15,0,178,181,1,0,0,0,179,181,3,30,15,0,180,175,1,0,
        0,0,180,179,1,0,0,0,181,29,1,0,0,0,182,183,3,32,16,0,183,184,3,22,
        11,0,184,185,3,32,16,0,185,188,1,0,0,0,186,188,3,32,16,0,187,182,
        1,0,0,0,187,186,1,0,0,0,188,31,1,0,0,0,189,190,6,16,-1,0,190,191,
        3,34,17,0,191,198,1,0,0,0,192,193,10,2,0,0,193,194,3,20,10,0,194,
        195,3,34,17,0,195,197,1,0,0,0,196,192,1,0,0,0,197,200,1,0,0,0,198,
        196,1,0,0,0,198,199,1,0,0,0,199,33,1,0,0,0,200,198,1,0,0,0,201,202,
        6,17,-1,0,202,203,3,36,18,0,203,210,1,0,0,0,204,205,10,2,0,0,205,
        206,3,18,9,0,206,207,3,36,18,0,207,209,1,0,0,0,208,204,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,35,1,0,0,0,212,210,
        1,0,0,0,213,214,6,18,-1,0,214,215,3,38,19,0,215,222,1,0,0,0,216,
        217,10,2,0,0,217,218,3,16,8,0,218,219,3,38,19,0,219,221,1,0,0,0,
        220,216,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,
        223,37,1,0,0,0,224,222,1,0,0,0,225,226,3,14,7,0,226,227,3,38,19,
        0,227,230,1,0,0,0,228,230,3,40,20,0,229,225,1,0,0,0,229,228,1,0,
        0,0,230,39,1,0,0,0,231,232,3,12,6,0,232,233,3,40,20,0,233,236,1,
        0,0,0,234,236,3,42,21,0,235,231,1,0,0,0,235,234,1,0,0,0,236,41,1,
        0,0,0,237,240,3,10,5,0,238,240,3,44,22,0,239,237,1,0,0,0,239,238,
        1,0,0,0,240,43,1,0,0,0,241,252,5,45,0,0,242,252,5,46,0,0,243,252,
        5,47,0,0,244,252,5,48,0,0,245,252,3,70,35,0,246,252,3,108,54,0,247,
        248,5,4,0,0,248,249,3,26,13,0,249,250,5,5,0,0,250,252,1,0,0,0,251,
        241,1,0,0,0,251,242,1,0,0,0,251,243,1,0,0,0,251,244,1,0,0,0,251,
        245,1,0,0,0,251,246,1,0,0,0,251,247,1,0,0,0,252,45,1,0,0,0,253,254,
        7,4,0,0,254,47,1,0,0,0,255,259,3,46,23,0,256,259,5,15,0,0,257,259,
        5,16,0,0,258,255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,49,
        1,0,0,0,260,262,3,52,26,0,261,263,5,9,0,0,262,261,1,0,0,0,263,264,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,279,1,0,0,0,266,268,
        3,62,31,0,267,269,5,9,0,0,268,267,1,0,0,0,269,270,1,0,0,0,270,268,
        1,0,0,0,270,271,1,0,0,0,271,279,1,0,0,0,272,274,3,74,37,0,273,275,
        5,9,0,0,274,273,1,0,0,0,275,276,1,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,279,1,0,0,0,278,260,1,0,0,0,278,266,1,0,0,0,278,272,
        1,0,0,0,279,51,1,0,0,0,280,284,3,54,27,0,281,284,3,56,28,0,282,284,
        3,58,29,0,283,280,1,0,0,0,283,281,1,0,0,0,283,282,1,0,0,0,284,53,
        1,0,0,0,285,286,3,46,23,0,286,287,5,45,0,0,287,288,3,60,30,0,288,
        293,1,0,0,0,289,290,3,46,23,0,290,291,5,45,0,0,291,293,1,0,0,0,292,
        285,1,0,0,0,292,289,1,0,0,0,293,55,1,0,0,0,294,295,5,16,0,0,295,
        296,5,45,0,0,296,300,3,60,30,0,297,298,5,16,0,0,298,300,5,45,0,0,
        299,294,1,0,0,0,299,297,1,0,0,0,300,57,1,0,0,0,301,302,5,15,0,0,
        302,303,5,45,0,0,303,304,3,60,30,0,304,59,1,0,0,0,305,306,5,33,0,
        0,306,307,3,26,13,0,307,61,1,0,0,0,308,309,3,46,23,0,309,310,3,64,
        32,0,310,311,3,68,34,0,311,316,1,0,0,0,312,313,3,46,23,0,313,314,
        3,64,32,0,314,316,1,0,0,0,315,308,1,0,0,0,315,312,1,0,0,0,316,63,
        1,0,0,0,317,318,5,45,0,0,318,319,5,6,0,0,319,320,3,66,33,0,320,321,
        5,7,0,0,321,65,1,0,0,0,322,323,5,46,0,0,323,324,5,8,0,0,324,327,
        3,66,33,0,325,327,5,46,0,0,326,322,1,0,0,0,326,325,1,0,0,0,327,67,
        1,0,0,0,328,329,5,33,0,0,329,330,3,70,35,0,330,69,1,0,0,0,331,332,
        5,6,0,0,332,333,3,72,36,0,333,334,5,7,0,0,334,71,1,0,0,0,335,336,
        3,26,13,0,336,337,5,8,0,0,337,338,3,72,36,0,338,341,1,0,0,0,339,
        341,3,26,13,0,340,335,1,0,0,0,340,339,1,0,0,0,341,73,1,0,0,0,342,
        343,5,17,0,0,343,344,5,45,0,0,344,345,5,4,0,0,345,346,3,76,38,0,
        346,350,5,5,0,0,347,349,5,9,0,0,348,347,1,0,0,0,349,352,1,0,0,0,
        350,348,1,0,0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,
        353,354,3,82,41,0,354,75,1,0,0,0,355,356,3,80,40,0,356,357,3,78,
        39,0,357,360,1,0,0,0,358,360,1,0,0,0,359,355,1,0,0,0,359,358,1,0,
        0,0,360,77,1,0,0,0,361,362,5,8,0,0,362,363,3,80,40,0,363,364,3,78,
        39,0,364,367,1,0,0,0,365,367,1,0,0,0,366,361,1,0,0,0,366,365,1,0,
        0,0,367,79,1,0,0,0,368,369,3,46,23,0,369,370,5,45,0,0,370,375,1,
        0,0,0,371,372,3,46,23,0,372,373,3,64,32,0,373,375,1,0,0,0,374,368,
        1,0,0,0,374,371,1,0,0,0,375,81,1,0,0,0,376,380,3,106,53,0,377,380,
        3,114,57,0,378,380,1,0,0,0,379,376,1,0,0,0,379,377,1,0,0,0,379,378,
        1,0,0,0,380,83,1,0,0,0,381,383,3,52,26,0,382,384,5,9,0,0,383,382,
        1,0,0,0,384,385,1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,432,
        1,0,0,0,387,389,3,62,31,0,388,390,5,9,0,0,389,388,1,0,0,0,390,391,
        1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,432,1,0,0,0,393,395,
        3,86,43,0,394,396,5,9,0,0,395,394,1,0,0,0,396,397,1,0,0,0,397,395,
        1,0,0,0,397,398,1,0,0,0,398,432,1,0,0,0,399,432,3,96,48,0,400,432,
        3,100,50,0,401,403,3,102,51,0,402,404,5,9,0,0,403,402,1,0,0,0,404,
        405,1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,432,1,0,0,0,407,
        409,3,104,52,0,408,410,5,9,0,0,409,408,1,0,0,0,410,411,1,0,0,0,411,
        409,1,0,0,0,411,412,1,0,0,0,412,432,1,0,0,0,413,415,3,106,53,0,414,
        416,5,9,0,0,415,414,1,0,0,0,416,417,1,0,0,0,417,415,1,0,0,0,417,
        418,1,0,0,0,418,432,1,0,0,0,419,421,3,108,54,0,420,422,5,9,0,0,421,
        420,1,0,0,0,422,423,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,
        432,1,0,0,0,425,427,3,114,57,0,426,428,5,9,0,0,427,426,1,0,0,0,428,
        429,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,432,1,0,0,0,431,
        381,1,0,0,0,431,387,1,0,0,0,431,393,1,0,0,0,431,399,1,0,0,0,431,
        400,1,0,0,0,431,401,1,0,0,0,431,407,1,0,0,0,431,413,1,0,0,0,431,
        419,1,0,0,0,431,425,1,0,0,0,432,85,1,0,0,0,433,434,3,88,44,0,434,
        435,3,60,30,0,435,87,1,0,0,0,436,439,5,45,0,0,437,439,3,4,2,0,438,
        436,1,0,0,0,438,437,1,0,0,0,439,89,1,0,0,0,440,441,5,23,0,0,441,
        442,5,4,0,0,442,443,3,26,13,0,443,447,5,5,0,0,444,446,5,9,0,0,445,
        444,1,0,0,0,446,449,1,0,0,0,447,445,1,0,0,0,447,448,1,0,0,0,448,
        450,1,0,0,0,449,447,1,0,0,0,450,451,3,84,42,0,451,91,1,0,0,0,452,
        453,5,25,0,0,453,454,5,4,0,0,454,455,3,26,13,0,455,459,5,5,0,0,456,
        458,5,9,0,0,457,456,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,
        460,1,0,0,0,460,462,1,0,0,0,461,459,1,0,0,0,462,463,3,84,42,0,463,
        93,1,0,0,0,464,468,5,24,0,0,465,467,5,9,0,0,466,465,1,0,0,0,467,
        470,1,0,0,0,468,466,1,0,0,0,468,469,1,0,0,0,469,471,1,0,0,0,470,
        468,1,0,0,0,471,474,3,84,42,0,472,474,1,0,0,0,473,464,1,0,0,0,473,
        472,1,0,0,0,474,95,1,0,0,0,475,479,3,90,45,0,476,478,5,9,0,0,477,
        476,1,0,0,0,478,481,1,0,0,0,479,477,1,0,0,0,479,480,1,0,0,0,480,
        482,1,0,0,0,481,479,1,0,0,0,482,483,3,98,49,0,483,484,3,94,47,0,
        484,97,1,0,0,0,485,489,3,92,46,0,486,488,5,9,0,0,487,486,1,0,0,0,
        488,491,1,0,0,0,489,487,1,0,0,0,489,490,1,0,0,0,490,492,1,0,0,0,
        491,489,1,0,0,0,492,493,3,98,49,0,493,496,1,0,0,0,494,496,1,0,0,
        0,495,485,1,0,0,0,495,494,1,0,0,0,496,99,1,0,0,0,497,498,5,18,0,
        0,498,499,5,45,0,0,499,500,5,19,0,0,500,501,3,26,13,0,501,502,5,
        20,0,0,502,506,3,26,13,0,503,505,5,9,0,0,504,503,1,0,0,0,505,508,
        1,0,0,0,506,504,1,0,0,0,506,507,1,0,0,0,507,509,1,0,0,0,508,506,
        1,0,0,0,509,510,3,84,42,0,510,101,1,0,0,0,511,512,5,21,0,0,512,103,
        1,0,0,0,513,514,5,22,0,0,514,105,1,0,0,0,515,516,5,14,0,0,516,519,
        3,26,13,0,517,519,5,14,0,0,518,515,1,0,0,0,518,517,1,0,0,0,519,107,
        1,0,0,0,520,521,5,45,0,0,521,522,5,4,0,0,522,523,3,110,55,0,523,
        524,5,5,0,0,524,109,1,0,0,0,525,526,3,26,13,0,526,527,3,112,56,0,
        527,530,1,0,0,0,528,530,1,0,0,0,529,525,1,0,0,0,529,528,1,0,0,0,
        530,111,1,0,0,0,531,532,5,8,0,0,532,533,3,26,13,0,533,534,3,112,
        56,0,534,537,1,0,0,0,535,537,1,0,0,0,536,531,1,0,0,0,536,535,1,0,
        0,0,537,113,1,0,0,0,538,540,5,26,0,0,539,541,5,9,0,0,540,539,1,0,
        0,0,541,542,1,0,0,0,542,540,1,0,0,0,542,543,1,0,0,0,543,544,1,0,
        0,0,544,545,3,116,58,0,545,546,5,27,0,0,546,115,1,0,0,0,547,548,
        3,84,42,0,548,549,3,116,58,0,549,552,1,0,0,0,550,552,1,0,0,0,551,
        547,1,0,0,0,551,550,1,0,0,0,552,117,1,0,0,0,53,124,133,137,144,155,
        180,187,198,210,222,229,235,239,251,258,264,270,276,278,283,292,
        299,315,326,340,350,359,366,374,379,385,391,397,405,411,417,423,
        429,431,438,447,459,468,473,479,489,495,506,518,529,536,542,551
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "'\\r'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'...'", "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", 
                      "SB_RIGHTBRACKET", "SB_LEFTSQUARE", "SB_RIGHTSQUARE", 
                      "SB_COMMA", "SB_NEWLINE", "SB_CR", "KW_NUMBER", "KW_BOOL", 
                      "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                      "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                      "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                      "KW_END", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", 
                      "OP_MOD", "OP_ASSIGN", "OP_EQUAL_NUM", "OP_UNEQUAL", 
                      "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", "OP_MOREOREQUAL", 
                      "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", "OP_AND", "OP_OR", 
                      "IDENTIFIER", "NUMBER", "BOOL", "STRING", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declarationLst = 1
    RULE_arrayElement = 2
    RULE_expr_element = 3
    RULE_op_index = 4
    RULE_op_unary_index = 5
    RULE_op_unary_sign = 6
    RULE_op_unary_logical = 7
    RULE_op_binary_multiplying = 8
    RULE_op_binary_adding = 9
    RULE_op_binary_logical = 10
    RULE_op_binary_relational = 11
    RULE_op_binary_string = 12
    RULE_expr = 13
    RULE_expr_string = 14
    RULE_expr_relational = 15
    RULE_expr_logical = 16
    RULE_expr_adding = 17
    RULE_expr_multiplying = 18
    RULE_expr_not = 19
    RULE_expr_sign = 20
    RULE_expr_index = 21
    RULE_operand = 22
    RULE_kw_type_explicit = 23
    RULE_kw_type = 24
    RULE_stmt_declaration = 25
    RULE_stmt_var_declaration = 26
    RULE_stmt_var_declaration_explicit = 27
    RULE_stmt_var_declaration_dynamic = 28
    RULE_stmt_var_declaration_var = 29
    RULE_value_init = 30
    RULE_stmt_array_declaration = 31
    RULE_arrayId = 32
    RULE_arrayDim = 33
    RULE_array_init = 34
    RULE_arrayValue = 35
    RULE_exprLst = 36
    RULE_stmt_func_declaration = 37
    RULE_paramLst = 38
    RULE_paramLstTail = 39
    RULE_param = 40
    RULE_func_body = 41
    RULE_statement = 42
    RULE_stmt_assignment = 43
    RULE_assignment_lhs = 44
    RULE_if_statement = 45
    RULE_elif_statement = 46
    RULE_else_statement = 47
    RULE_stmt_if = 48
    RULE_elifLst = 49
    RULE_stmt_for = 50
    RULE_stmt_break = 51
    RULE_stmt_continue = 52
    RULE_stmt_return = 53
    RULE_stmt_func_call = 54
    RULE_argLst = 55
    RULE_argLstTail = 56
    RULE_stmt_block = 57
    RULE_statementLst = 58

    ruleNames =  [ "program", "declarationLst", "arrayElement", "expr_element", 
                   "op_index", "op_unary_index", "op_unary_sign", "op_unary_logical", 
                   "op_binary_multiplying", "op_binary_adding", "op_binary_logical", 
                   "op_binary_relational", "op_binary_string", "expr", "expr_string", 
                   "expr_relational", "expr_logical", "expr_adding", "expr_multiplying", 
                   "expr_not", "expr_sign", "expr_index", "operand", "kw_type_explicit", 
                   "kw_type", "stmt_declaration", "stmt_var_declaration", 
                   "stmt_var_declaration_explicit", "stmt_var_declaration_dynamic", 
                   "stmt_var_declaration_var", "value_init", "stmt_array_declaration", 
                   "arrayId", "arrayDim", "array_init", "arrayValue", "exprLst", 
                   "stmt_func_declaration", "paramLst", "paramLstTail", 
                   "param", "func_body", "statement", "stmt_assignment", 
                   "assignment_lhs", "if_statement", "elif_statement", "else_statement", 
                   "stmt_if", "elifLst", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "argLst", "argLstTail", 
                   "stmt_block", "statementLst" ]

    EOF = Token.EOF
    COMMENT=1
    WS=2
    WS2=3
    SB_LEFTBRACKET=4
    SB_RIGHTBRACKET=5
    SB_LEFTSQUARE=6
    SB_RIGHTSQUARE=7
    SB_COMMA=8
    SB_NEWLINE=9
    SB_CR=10
    KW_NUMBER=11
    KW_BOOL=12
    KW_STRING=13
    KW_RETURN=14
    KW_VAR=15
    KW_DYNAMIC=16
    KW_FUNC=17
    KW_FOR=18
    KW_UNTIL=19
    KW_BY=20
    KW_BREAK=21
    KW_CONTINUE=22
    KW_IF=23
    KW_ELSE=24
    KW_ELIF=25
    KW_BEGIN=26
    KW_END=27
    OP_PLUS=28
    OP_MINUS=29
    OP_MULT=30
    OP_DIV=31
    OP_MOD=32
    OP_ASSIGN=33
    OP_EQUAL_NUM=34
    OP_UNEQUAL=35
    OP_LESS=36
    OP_MORE=37
    OP_LESSOREQUAL=38
    OP_MOREOREQUAL=39
    OP_CONCAT=40
    OP_EQUAL_STR=41
    OP_NOT=42
    OP_AND=43
    OP_OR=44
    IDENTIFIER=45
    NUMBER=46
    BOOL=47
    STRING=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.declarationLst()
            self.state = 119
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_declarationContext,0)


        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_declarationLst




    def declarationLst(self):

        localctx = ZCodeParser.DeclarationLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationLst)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 121
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self.stmt_declaration()
                self.state = 128
                self.declarationLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 130
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self.stmt_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr_element(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_elementContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayElement




    def arrayElement(self):

        localctx = ZCodeParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrayElement)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 140
                self.expr_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.stmt_func_call()
                self.state = 142
                self.expr_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_element




    def expr_element(self):

        localctx = ZCodeParser.Expr_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 147
            self.op_index()
            self.state = 148
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_index




    def op_index(self):

        localctx = ZCodeParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op_index)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.expr()
                self.state = 151
                self.match(ZCodeParser.SB_COMMA)
                self.state = 152
                self.op_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_index




    def op_unary_index(self):

        localctx = ZCodeParser.Op_unary_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.arrayElement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_sign




    def op_unary_sign(self):

        localctx = ZCodeParser.Op_unary_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.OP_MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_logical




    def op_unary_logical(self):

        localctx = ZCodeParser.Op_unary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZCodeParser.OP_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULT(self):
            return self.getToken(ZCodeParser.OP_MULT, 0)

        def OP_DIV(self):
            return self.getToken(ZCodeParser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(ZCodeParser.OP_MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_multiplying




    def op_binary_multiplying(self):

        localctx = ZCodeParser.Op_binary_multiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_PLUS(self):
            return self.getToken(ZCodeParser.OP_PLUS, 0)

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_adding




    def op_binary_adding(self):

        localctx = ZCodeParser.Op_binary_addingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_AND(self):
            return self.getToken(ZCodeParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(ZCodeParser.OP_OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_logical




    def op_binary_logical(self):

        localctx = ZCodeParser.Op_binary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EQUAL_NUM(self):
            return self.getToken(ZCodeParser.OP_EQUAL_NUM, 0)

        def OP_EQUAL_STR(self):
            return self.getToken(ZCodeParser.OP_EQUAL_STR, 0)

        def OP_UNEQUAL(self):
            return self.getToken(ZCodeParser.OP_UNEQUAL, 0)

        def OP_LESS(self):
            return self.getToken(ZCodeParser.OP_LESS, 0)

        def OP_MORE(self):
            return self.getToken(ZCodeParser.OP_MORE, 0)

        def OP_LESSOREQUAL(self):
            return self.getToken(ZCodeParser.OP_LESSOREQUAL, 0)

        def OP_MOREOREQUAL(self):
            return self.getToken(ZCodeParser.OP_MOREOREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_relational




    def op_binary_relational(self):

        localctx = ZCodeParser.Op_binary_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3281355014144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_CONCAT(self):
            return self.getToken(ZCodeParser.OP_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_string




    def op_binary_string(self):

        localctx = ZCodeParser.Op_binary_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(ZCodeParser.OP_CONCAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.expr_string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,i)


        def op_binary_string(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string




    def expr_string(self):

        localctx = ZCodeParser.Expr_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_string)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expr_relational()
                self.state = 176
                self.op_binary_string()
                self.state = 177
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.expr_relational()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_logicalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,i)


        def op_binary_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_relationalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_relational




    def expr_relational(self):

        localctx = ZCodeParser.Expr_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_relational)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expr_logical(0)
                self.state = 183
                self.op_binary_relational()
                self.state = 184
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.expr_logical(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def op_binary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_logicalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_logical



    def expr_logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_logicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    self.op_binary_logical()
                    self.state = 194
                    self.expr_adding(0) 
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def op_binary_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_addingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_adding



    def expr_adding(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_addingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_adding, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    self.op_binary_adding()
                    self.state = 206
                    self.expr_multiplying(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def op_binary_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_multiplyingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_multiplying



    def expr_multiplying(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_multiplyingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_multiplying, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    self.op_binary_multiplying()
                    self.state = 218
                    self.expr_not() 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_logicalContext,0)


        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_not




    def expr_not(self):

        localctx = ZCodeParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_not)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.op_unary_logical()
                self.state = 226
                self.expr_not()
                pass
            elif token in [4, 6, 29, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.expr_sign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_signContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def expr_index(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_sign




    def expr_sign(self):

        localctx = ZCodeParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_sign)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.op_unary_sign()
                self.state = 232
                self.expr_sign()
                pass
            elif token in [4, 6, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.expr_index()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_indexContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_index




    def expr_index(self):

        localctx = ZCodeParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_index)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.op_unary_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                self.arrayValue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.stmt_func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 247
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 248
                self.expr()
                self.state = 249
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kw_type_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type_explicit




    def kw_type_explicit(self):

        localctx = ZCodeParser.Kw_type_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_kw_type_explicit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kw_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type




    def kw_type(self):

        localctx = ZCodeParser.Kw_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_kw_type)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.kw_type_explicit()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(ZCodeParser.KW_DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_func_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_declaration




    def stmt_declaration(self):

        localctx = ZCodeParser.Stmt_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_declaration)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.stmt_var_declaration()
                self.state = 262 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 261
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 264 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.stmt_array_declaration()
                self.state = 268 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 267
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 270 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.stmt_func_declaration()
                self.state = 274 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 273
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 276 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_explicitContext,0)


        def stmt_var_declaration_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_dynamicContext,0)


        def stmt_var_declaration_var(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_var_declaration)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.stmt_var_declaration_explicit()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.stmt_var_declaration_dynamic()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.stmt_var_declaration_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_explicit




    def stmt_var_declaration_explicit(self):

        localctx = ZCodeParser.Stmt_var_declaration_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_var_declaration_explicit)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.kw_type_explicit()
                self.state = 286
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 287
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.kw_type_explicit()
                self.state = 290
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_dynamic




    def stmt_var_declaration_dynamic(self):

        localctx = ZCodeParser.Stmt_var_declaration_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_var_declaration_dynamic)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 295
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 296
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 298
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_var




    def stmt_var_declaration_var(self):

        localctx = ZCodeParser.Stmt_var_declaration_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_var_declaration_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.KW_VAR)
            self.state = 302
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 303
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 306
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_array_declaration




    def stmt_array_declaration(self):

        localctx = ZCodeParser.Stmt_array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_array_declaration)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.kw_type_explicit()
                self.state = 309
                self.arrayId()
                self.state = 310
                self.array_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.kw_type_explicit()
                self.state = 313
                self.arrayId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayId




    def arrayId(self):

        localctx = ZCodeParser.ArrayIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 318
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 319
            self.arrayDim()
            self.state = 320
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDim




    def arrayDim(self):

        localctx = ZCodeParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayDim)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(ZCodeParser.NUMBER)
                self.state = 323
                self.match(ZCodeParser.SB_COMMA)
                self.state = 324
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 329
            self.arrayValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayValue




    def arrayValue(self):

        localctx = ZCodeParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 332
            self.exprLst()
            self.state = 333
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprLst




    def exprLst(self):

        localctx = ZCodeParser.ExprLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exprLst)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expr()
                self.state = 336
                self.match(ZCodeParser.SB_COMMA)
                self.state = 337
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_declaration




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.KW_FUNC)
            self.state = 343
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 344
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 345
            self.paramLst()
            self.state = 346
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 347
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 353
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_paramLst)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.param()
                self.state = 356
                self.paramLstTail()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLstTail




    def paramLstTail(self):

        localctx = ZCodeParser.ParamLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_paramLstTail)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(ZCodeParser.SB_COMMA)
                self.state = 362
                self.param()
                self.state = 363
                self.paramLstTail()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_param)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.kw_type_explicit()
                self.state = 369
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.kw_type_explicit()
                self.state = 372
                self.arrayId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func_body)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.stmt_return()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.stmt_block()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_assignment(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assignmentContext,0)


        def stmt_if(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_ifContext,0)


        def stmt_for(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_forContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_continueContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statement)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.stmt_var_declaration()
                self.state = 383 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 382
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 385 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.stmt_array_declaration()
                self.state = 389 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 388
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 391 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.stmt_assignment()
                self.state = 395 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 394
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 397 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.stmt_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 400
                self.stmt_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 401
                self.stmt_break()
                self.state = 403 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 402
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 405 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 407
                self.stmt_continue()
                self.state = 409 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 408
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 411 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 413
                self.stmt_return()
                self.state = 415 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 414
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 417 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 419
                self.stmt_func_call()
                self.state = 421 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 420
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 423 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 425
                self.stmt_block()
                self.state = 427 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 426
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 429 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_lhsContext,0)


        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assignment




    def stmt_assignment(self):

        localctx = ZCodeParser.Stmt_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.assignment_lhs()
            self.state = 434
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_lhs




    def assignment_lhs(self):

        localctx = ZCodeParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assignment_lhs)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.arrayElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(ZCodeParser.KW_IF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(ZCodeParser.KW_IF)
            self.state = 441
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 442
            self.expr()
            self.state = 443
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 444
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 450
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELIF(self):
            return self.getToken(ZCodeParser.KW_ELIF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(ZCodeParser.KW_ELIF)
            self.state = 453
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 454
            self.expr()
            self.state = 455
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 456
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 462
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(ZCodeParser.KW_ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(ZCodeParser.KW_ELSE)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 465
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 470
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 471
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.if_statement()
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 476
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 482
            self.elifLst()
            self.state = 483
            self.else_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elifLst)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.elif_statement()
                self.state = 489
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 486
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 491
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                self.state = 492
                self.elifLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(ZCodeParser.KW_FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def KW_UNTIL(self):
            return self.getToken(ZCodeParser.KW_UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def KW_BY(self):
            return self.getToken(ZCodeParser.KW_BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmt_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(ZCodeParser.KW_FOR)
            self.state = 498
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 499
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 500
            self.expr()
            self.state = 501
            self.match(ZCodeParser.KW_BY)
            self.state = 502
            self.expr()
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 503
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 509
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(ZCodeParser.KW_BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_break




    def stmt_break(self):

        localctx = ZCodeParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(ZCodeParser.KW_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(ZCodeParser.KW_CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_continue




    def stmt_continue(self):

        localctx = ZCodeParser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(ZCodeParser.KW_CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(ZCodeParser.KW_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_return)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(ZCodeParser.KW_RETURN)
                self.state = 516
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(ZCodeParser.KW_RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def argLst(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 521
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 522
            self.argLst()
            self.state = 523
            self.match(ZCodeParser.SB_RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLst




    def argLst(self):

        localctx = ZCodeParser.ArgLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_argLst)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 6, 29, 42, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.expr()
                self.state = 526
                self.argLstTail()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLstTail




    def argLstTail(self):

        localctx = ZCodeParser.ArgLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_argLstTail)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(ZCodeParser.SB_COMMA)
                self.state = 532
                self.expr()
                self.state = 533
                self.argLstTail()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BEGIN(self):
            return self.getToken(ZCodeParser.KW_BEGIN, 0)

        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 540 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 539
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 542 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 544
            self.statementLst()
            self.state = 545
            self.match(ZCodeParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementLst




    def statementLst(self):

        localctx = ZCodeParser.StatementLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_statementLst)
        try:
            self.state = 551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 16, 18, 21, 22, 23, 26, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.statement()
                self.state = 548
                self.statementLst()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_logical_sempred
        self._predicates[17] = self.expr_adding_sempred
        self._predicates[18] = self.expr_multiplying_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_logical_sempred(self, localctx:Expr_logicalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_adding_sempred(self, localctx:Expr_addingContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_multiplying_sempred(self, localctx:Expr_multiplyingContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




