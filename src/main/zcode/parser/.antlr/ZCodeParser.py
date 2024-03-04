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
        4,1,51,492,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,135,8,1,1,2,1,2,1,2,3,2,140,8,2,1,3,1,3,1,3,3,3,145,8,3,1,4,
        1,4,1,4,1,4,1,4,3,4,152,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        3,6,163,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,
        1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,188,
        8,16,1,17,1,17,1,17,1,17,1,17,3,17,195,8,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,5,18,204,8,18,10,18,12,18,207,9,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,216,8,19,10,19,12,19,219,9,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,5,20,228,8,20,10,20,12,20,231,9,20,1,21,
        1,21,1,21,1,21,3,21,237,8,21,1,22,1,22,1,22,1,22,3,22,243,8,22,1,
        23,1,23,3,23,247,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,3,24,259,8,24,1,25,1,25,1,26,1,26,1,26,3,26,266,8,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,277,8,27,1,28,1,28,
        1,28,3,28,282,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,291,8,
        29,1,30,1,30,1,30,1,30,1,30,3,30,298,8,30,1,31,1,31,1,31,1,31,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,314,8,33,1,
        34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,3,35,325,8,35,1,36,1,
        36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,3,38,339,8,
        38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,3,
        40,353,8,40,1,41,1,41,1,41,1,41,1,41,3,41,360,8,41,1,42,1,42,1,42,
        1,42,1,42,1,42,3,42,368,8,42,1,43,1,43,1,43,3,43,373,8,43,1,44,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,401,
        8,44,1,45,1,45,1,46,1,46,1,46,1,47,1,47,3,47,410,8,47,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,
        1,50,1,50,1,50,1,50,3,50,431,8,50,1,51,1,51,1,51,1,51,1,51,1,52,
        1,52,1,52,1,52,1,52,3,52,443,8,52,1,53,1,53,1,53,1,53,1,53,1,53,
        1,53,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,56,3,56,461,8,56,
        1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,3,58,472,8,58,1,59,
        1,59,1,59,1,59,1,59,3,59,479,8,59,1,60,1,60,1,60,1,60,1,60,1,61,
        1,61,1,61,1,61,3,61,490,8,61,1,61,0,3,36,38,40,62,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,0,5,1,0,30,32,1,0,28,
        29,1,0,43,44,2,0,34,39,41,41,1,0,11,13,480,0,124,1,0,0,0,2,134,1,
        0,0,0,4,139,1,0,0,0,6,144,1,0,0,0,8,151,1,0,0,0,10,153,1,0,0,0,12,
        162,1,0,0,0,14,164,1,0,0,0,16,166,1,0,0,0,18,168,1,0,0,0,20,170,
        1,0,0,0,22,172,1,0,0,0,24,174,1,0,0,0,26,176,1,0,0,0,28,178,1,0,
        0,0,30,180,1,0,0,0,32,187,1,0,0,0,34,194,1,0,0,0,36,196,1,0,0,0,
        38,208,1,0,0,0,40,220,1,0,0,0,42,236,1,0,0,0,44,242,1,0,0,0,46,246,
        1,0,0,0,48,258,1,0,0,0,50,260,1,0,0,0,52,265,1,0,0,0,54,276,1,0,
        0,0,56,281,1,0,0,0,58,290,1,0,0,0,60,297,1,0,0,0,62,299,1,0,0,0,
        64,303,1,0,0,0,66,313,1,0,0,0,68,315,1,0,0,0,70,324,1,0,0,0,72,326,
        1,0,0,0,74,329,1,0,0,0,76,338,1,0,0,0,78,340,1,0,0,0,80,352,1,0,
        0,0,82,359,1,0,0,0,84,367,1,0,0,0,86,372,1,0,0,0,88,400,1,0,0,0,
        90,402,1,0,0,0,92,404,1,0,0,0,94,409,1,0,0,0,96,411,1,0,0,0,98,418,
        1,0,0,0,100,430,1,0,0,0,102,432,1,0,0,0,104,442,1,0,0,0,106,444,
        1,0,0,0,108,453,1,0,0,0,110,455,1,0,0,0,112,460,1,0,0,0,114,462,
        1,0,0,0,116,471,1,0,0,0,118,478,1,0,0,0,120,480,1,0,0,0,122,489,
        1,0,0,0,124,125,3,2,1,0,125,126,5,0,0,1,126,1,1,0,0,0,127,128,3,
        4,2,0,128,129,3,54,27,0,129,130,3,2,1,0,130,135,1,0,0,0,131,132,
        3,4,2,0,132,133,3,54,27,0,133,135,1,0,0,0,134,127,1,0,0,0,134,131,
        1,0,0,0,135,3,1,0,0,0,136,137,5,9,0,0,137,140,3,4,2,0,138,140,1,
        0,0,0,139,136,1,0,0,0,139,138,1,0,0,0,140,5,1,0,0,0,141,142,5,9,
        0,0,142,145,3,6,3,0,143,145,5,9,0,0,144,141,1,0,0,0,144,143,1,0,
        0,0,145,7,1,0,0,0,146,147,5,45,0,0,147,152,3,10,5,0,148,149,3,114,
        57,0,149,150,3,10,5,0,150,152,1,0,0,0,151,146,1,0,0,0,151,148,1,
        0,0,0,152,9,1,0,0,0,153,154,5,6,0,0,154,155,3,12,6,0,155,156,5,7,
        0,0,156,11,1,0,0,0,157,158,3,30,15,0,158,159,5,8,0,0,159,160,3,12,
        6,0,160,163,1,0,0,0,161,163,3,30,15,0,162,157,1,0,0,0,162,161,1,
        0,0,0,163,13,1,0,0,0,164,165,3,8,4,0,165,15,1,0,0,0,166,167,5,29,
        0,0,167,17,1,0,0,0,168,169,5,42,0,0,169,19,1,0,0,0,170,171,7,0,0,
        0,171,21,1,0,0,0,172,173,7,1,0,0,173,23,1,0,0,0,174,175,7,2,0,0,
        175,25,1,0,0,0,176,177,7,3,0,0,177,27,1,0,0,0,178,179,5,40,0,0,179,
        29,1,0,0,0,180,181,3,32,16,0,181,31,1,0,0,0,182,183,3,34,17,0,183,
        184,3,28,14,0,184,185,3,34,17,0,185,188,1,0,0,0,186,188,3,34,17,
        0,187,182,1,0,0,0,187,186,1,0,0,0,188,33,1,0,0,0,189,190,3,36,18,
        0,190,191,3,26,13,0,191,192,3,36,18,0,192,195,1,0,0,0,193,195,3,
        36,18,0,194,189,1,0,0,0,194,193,1,0,0,0,195,35,1,0,0,0,196,197,6,
        18,-1,0,197,198,3,38,19,0,198,205,1,0,0,0,199,200,10,2,0,0,200,201,
        3,24,12,0,201,202,3,38,19,0,202,204,1,0,0,0,203,199,1,0,0,0,204,
        207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,37,1,0,0,0,207,205,
        1,0,0,0,208,209,6,19,-1,0,209,210,3,40,20,0,210,217,1,0,0,0,211,
        212,10,2,0,0,212,213,3,22,11,0,213,214,3,40,20,0,214,216,1,0,0,0,
        215,211,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,
        218,39,1,0,0,0,219,217,1,0,0,0,220,221,6,20,-1,0,221,222,3,42,21,
        0,222,229,1,0,0,0,223,224,10,2,0,0,224,225,3,20,10,0,225,226,3,42,
        21,0,226,228,1,0,0,0,227,223,1,0,0,0,228,231,1,0,0,0,229,227,1,0,
        0,0,229,230,1,0,0,0,230,41,1,0,0,0,231,229,1,0,0,0,232,233,3,18,
        9,0,233,234,3,42,21,0,234,237,1,0,0,0,235,237,3,44,22,0,236,232,
        1,0,0,0,236,235,1,0,0,0,237,43,1,0,0,0,238,239,3,16,8,0,239,240,
        3,44,22,0,240,243,1,0,0,0,241,243,3,46,23,0,242,238,1,0,0,0,242,
        241,1,0,0,0,243,45,1,0,0,0,244,247,3,14,7,0,245,247,3,48,24,0,246,
        244,1,0,0,0,246,245,1,0,0,0,247,47,1,0,0,0,248,259,5,45,0,0,249,
        259,5,46,0,0,250,259,5,47,0,0,251,259,5,48,0,0,252,259,3,74,37,0,
        253,259,3,114,57,0,254,255,5,4,0,0,255,256,3,30,15,0,256,257,5,5,
        0,0,257,259,1,0,0,0,258,248,1,0,0,0,258,249,1,0,0,0,258,250,1,0,
        0,0,258,251,1,0,0,0,258,252,1,0,0,0,258,253,1,0,0,0,258,254,1,0,
        0,0,259,49,1,0,0,0,260,261,7,4,0,0,261,51,1,0,0,0,262,266,3,50,25,
        0,263,266,5,15,0,0,264,266,5,16,0,0,265,262,1,0,0,0,265,263,1,0,
        0,0,265,264,1,0,0,0,266,53,1,0,0,0,267,268,3,56,28,0,268,269,3,6,
        3,0,269,277,1,0,0,0,270,271,3,66,33,0,271,272,3,6,3,0,272,277,1,
        0,0,0,273,274,3,78,39,0,274,275,3,6,3,0,275,277,1,0,0,0,276,267,
        1,0,0,0,276,270,1,0,0,0,276,273,1,0,0,0,277,55,1,0,0,0,278,282,3,
        58,29,0,279,282,3,60,30,0,280,282,3,62,31,0,281,278,1,0,0,0,281,
        279,1,0,0,0,281,280,1,0,0,0,282,57,1,0,0,0,283,284,3,50,25,0,284,
        285,5,45,0,0,285,286,3,64,32,0,286,291,1,0,0,0,287,288,3,50,25,0,
        288,289,5,45,0,0,289,291,1,0,0,0,290,283,1,0,0,0,290,287,1,0,0,0,
        291,59,1,0,0,0,292,293,5,16,0,0,293,294,5,45,0,0,294,298,3,64,32,
        0,295,296,5,16,0,0,296,298,5,45,0,0,297,292,1,0,0,0,297,295,1,0,
        0,0,298,61,1,0,0,0,299,300,5,15,0,0,300,301,5,45,0,0,301,302,3,64,
        32,0,302,63,1,0,0,0,303,304,5,33,0,0,304,305,3,30,15,0,305,65,1,
        0,0,0,306,307,3,50,25,0,307,308,3,68,34,0,308,309,3,72,36,0,309,
        314,1,0,0,0,310,311,3,50,25,0,311,312,3,68,34,0,312,314,1,0,0,0,
        313,306,1,0,0,0,313,310,1,0,0,0,314,67,1,0,0,0,315,316,5,45,0,0,
        316,317,5,6,0,0,317,318,3,70,35,0,318,319,5,7,0,0,319,69,1,0,0,0,
        320,321,5,46,0,0,321,322,5,8,0,0,322,325,3,70,35,0,323,325,5,46,
        0,0,324,320,1,0,0,0,324,323,1,0,0,0,325,71,1,0,0,0,326,327,5,33,
        0,0,327,328,3,74,37,0,328,73,1,0,0,0,329,330,5,6,0,0,330,331,3,76,
        38,0,331,332,5,7,0,0,332,75,1,0,0,0,333,334,3,30,15,0,334,335,5,
        8,0,0,335,336,3,76,38,0,336,339,1,0,0,0,337,339,3,30,15,0,338,333,
        1,0,0,0,338,337,1,0,0,0,339,77,1,0,0,0,340,341,5,17,0,0,341,342,
        5,45,0,0,342,343,5,4,0,0,343,344,3,80,40,0,344,345,5,5,0,0,345,346,
        3,4,2,0,346,347,3,86,43,0,347,79,1,0,0,0,348,349,3,84,42,0,349,350,
        3,82,41,0,350,353,1,0,0,0,351,353,1,0,0,0,352,348,1,0,0,0,352,351,
        1,0,0,0,353,81,1,0,0,0,354,355,5,8,0,0,355,356,3,84,42,0,356,357,
        3,82,41,0,357,360,1,0,0,0,358,360,1,0,0,0,359,354,1,0,0,0,359,358,
        1,0,0,0,360,83,1,0,0,0,361,362,3,50,25,0,362,363,5,45,0,0,363,368,
        1,0,0,0,364,365,3,50,25,0,365,366,3,68,34,0,366,368,1,0,0,0,367,
        361,1,0,0,0,367,364,1,0,0,0,368,85,1,0,0,0,369,373,3,112,56,0,370,
        373,3,120,60,0,371,373,1,0,0,0,372,369,1,0,0,0,372,370,1,0,0,0,372,
        371,1,0,0,0,373,87,1,0,0,0,374,375,3,56,28,0,375,376,3,6,3,0,376,
        401,1,0,0,0,377,378,3,66,33,0,378,379,3,6,3,0,379,401,1,0,0,0,380,
        381,3,92,46,0,381,382,3,6,3,0,382,401,1,0,0,0,383,401,3,102,51,0,
        384,401,3,106,53,0,385,386,3,108,54,0,386,387,3,6,3,0,387,401,1,
        0,0,0,388,389,3,110,55,0,389,390,3,6,3,0,390,401,1,0,0,0,391,392,
        3,112,56,0,392,393,3,6,3,0,393,401,1,0,0,0,394,395,3,114,57,0,395,
        396,3,6,3,0,396,401,1,0,0,0,397,398,3,120,60,0,398,399,3,6,3,0,399,
        401,1,0,0,0,400,374,1,0,0,0,400,377,1,0,0,0,400,380,1,0,0,0,400,
        383,1,0,0,0,400,384,1,0,0,0,400,385,1,0,0,0,400,388,1,0,0,0,400,
        391,1,0,0,0,400,394,1,0,0,0,400,397,1,0,0,0,401,89,1,0,0,0,402,403,
        3,88,44,0,403,91,1,0,0,0,404,405,3,94,47,0,405,406,3,64,32,0,406,
        93,1,0,0,0,407,410,5,45,0,0,408,410,3,8,4,0,409,407,1,0,0,0,409,
        408,1,0,0,0,410,95,1,0,0,0,411,412,5,23,0,0,412,413,5,4,0,0,413,
        414,3,30,15,0,414,415,5,5,0,0,415,416,3,4,2,0,416,417,3,90,45,0,
        417,97,1,0,0,0,418,419,5,25,0,0,419,420,5,4,0,0,420,421,3,30,15,
        0,421,422,5,5,0,0,422,423,3,4,2,0,423,424,3,90,45,0,424,99,1,0,0,
        0,425,426,5,24,0,0,426,427,3,4,2,0,427,428,3,90,45,0,428,431,1,0,
        0,0,429,431,1,0,0,0,430,425,1,0,0,0,430,429,1,0,0,0,431,101,1,0,
        0,0,432,433,3,96,48,0,433,434,3,4,2,0,434,435,3,104,52,0,435,436,
        3,100,50,0,436,103,1,0,0,0,437,438,3,98,49,0,438,439,3,4,2,0,439,
        440,3,104,52,0,440,443,1,0,0,0,441,443,1,0,0,0,442,437,1,0,0,0,442,
        441,1,0,0,0,443,105,1,0,0,0,444,445,5,18,0,0,445,446,5,45,0,0,446,
        447,5,19,0,0,447,448,3,30,15,0,448,449,5,20,0,0,449,450,3,30,15,
        0,450,451,3,4,2,0,451,452,3,90,45,0,452,107,1,0,0,0,453,454,5,21,
        0,0,454,109,1,0,0,0,455,456,5,22,0,0,456,111,1,0,0,0,457,458,5,14,
        0,0,458,461,3,30,15,0,459,461,5,14,0,0,460,457,1,0,0,0,460,459,1,
        0,0,0,461,113,1,0,0,0,462,463,5,45,0,0,463,464,5,4,0,0,464,465,3,
        116,58,0,465,466,5,5,0,0,466,115,1,0,0,0,467,468,3,30,15,0,468,469,
        3,118,59,0,469,472,1,0,0,0,470,472,1,0,0,0,471,467,1,0,0,0,471,470,
        1,0,0,0,472,117,1,0,0,0,473,474,5,8,0,0,474,475,3,30,15,0,475,476,
        3,118,59,0,476,479,1,0,0,0,477,479,1,0,0,0,478,473,1,0,0,0,478,477,
        1,0,0,0,479,119,1,0,0,0,480,481,5,26,0,0,481,482,3,6,3,0,482,483,
        3,122,61,0,483,484,5,27,0,0,484,121,1,0,0,0,485,486,3,90,45,0,486,
        487,3,122,61,0,487,490,1,0,0,0,488,490,1,0,0,0,489,485,1,0,0,0,489,
        488,1,0,0,0,490,123,1,0,0,0,34,134,139,144,151,162,187,194,205,217,
        229,236,242,246,258,265,276,281,290,297,313,324,338,352,359,367,
        372,400,409,430,442,460,471,478,489
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
    RULE_newlineLst_0 = 2
    RULE_newlineLst_1 = 3
    RULE_arrayElement = 4
    RULE_expr_element = 5
    RULE_op_index = 6
    RULE_op_unary_index = 7
    RULE_op_unary_sign = 8
    RULE_op_unary_logical = 9
    RULE_op_binary_multiplying = 10
    RULE_op_binary_adding = 11
    RULE_op_binary_logical = 12
    RULE_op_binary_relational = 13
    RULE_op_binary_string = 14
    RULE_expr = 15
    RULE_expr_string = 16
    RULE_expr_relational = 17
    RULE_expr_logical = 18
    RULE_expr_adding = 19
    RULE_expr_multiplying = 20
    RULE_expr_not = 21
    RULE_expr_sign = 22
    RULE_expr_index = 23
    RULE_operand = 24
    RULE_kw_type_explicit = 25
    RULE_kw_type = 26
    RULE_stmt_declaration = 27
    RULE_stmt_var_declaration = 28
    RULE_stmt_var_declaration_explicit = 29
    RULE_stmt_var_declaration_dynamic = 30
    RULE_stmt_var_declaration_var = 31
    RULE_value_init = 32
    RULE_stmt_array_declaration = 33
    RULE_arrayId = 34
    RULE_arrayDim = 35
    RULE_array_init = 36
    RULE_arrayValue = 37
    RULE_exprLst = 38
    RULE_stmt_func_declaration = 39
    RULE_paramLst = 40
    RULE_paramLstTail = 41
    RULE_param = 42
    RULE_func_body = 43
    RULE_statement_type = 44
    RULE_statement = 45
    RULE_stmt_assignment = 46
    RULE_assignment_lhs = 47
    RULE_if_statement = 48
    RULE_elif_statement = 49
    RULE_else_statement = 50
    RULE_stmt_if = 51
    RULE_elifLst = 52
    RULE_stmt_for = 53
    RULE_stmt_break = 54
    RULE_stmt_continue = 55
    RULE_stmt_return = 56
    RULE_stmt_func_call = 57
    RULE_argLst = 58
    RULE_argLstTail = 59
    RULE_stmt_block = 60
    RULE_statementLst = 61

    ruleNames =  [ "program", "declarationLst", "newlineLst_0", "newlineLst_1", 
                   "arrayElement", "expr_element", "op_index", "op_unary_index", 
                   "op_unary_sign", "op_unary_logical", "op_binary_multiplying", 
                   "op_binary_adding", "op_binary_logical", "op_binary_relational", 
                   "op_binary_string", "expr", "expr_string", "expr_relational", 
                   "expr_logical", "expr_adding", "expr_multiplying", "expr_not", 
                   "expr_sign", "expr_index", "operand", "kw_type_explicit", 
                   "kw_type", "stmt_declaration", "stmt_var_declaration", 
                   "stmt_var_declaration_explicit", "stmt_var_declaration_dynamic", 
                   "stmt_var_declaration_var", "value_init", "stmt_array_declaration", 
                   "arrayId", "arrayDim", "array_init", "arrayValue", "exprLst", 
                   "stmt_func_declaration", "paramLst", "paramLstTail", 
                   "param", "func_body", "statement_type", "statement", 
                   "stmt_assignment", "assignment_lhs", "if_statement", 
                   "elif_statement", "else_statement", "stmt_if", "elifLst", 
                   "stmt_for", "stmt_break", "stmt_continue", "stmt_return", 
                   "stmt_func_call", "argLst", "argLstTail", "stmt_block", 
                   "statementLst" ]

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
            self.state = 124
            self.declarationLst()
            self.state = 125
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def stmt_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_declarationContext,0)


        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declarationLst




    def declarationLst(self):

        localctx = ZCodeParser.DeclarationLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationLst)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.newlineLst_0()
                self.state = 128
                self.stmt_declaration()
                self.state = 129
                self.declarationLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.newlineLst_0()
                self.state = 132
                self.stmt_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineLst_0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlineLst_0




    def newlineLst_0(self):

        localctx = ZCodeParser.NewlineLst_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newlineLst_0)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 137
                self.newlineLst_0()
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


    class NewlineLst_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlineLst_1




    def newlineLst_1(self):

        localctx = ZCodeParser.NewlineLst_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_newlineLst_1)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 142
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ZCodeParser.SB_NEWLINE)
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
        self.enterRule(localctx, 8, self.RULE_arrayElement)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 147
                self.expr_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.stmt_func_call()
                self.state = 149
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
        self.enterRule(localctx, 10, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 154
            self.op_index()
            self.state = 155
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
        self.enterRule(localctx, 12, self.RULE_op_index)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.expr()
                self.state = 158
                self.match(ZCodeParser.SB_COMMA)
                self.state = 159
                self.op_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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
        self.enterRule(localctx, 14, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 16, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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
        self.enterRule(localctx, 18, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
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
        self.enterRule(localctx, 20, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
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
        self.enterRule(localctx, 22, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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
        self.enterRule(localctx, 24, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
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
        self.enterRule(localctx, 26, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 28, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
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
        self.enterRule(localctx, 32, self.RULE_expr_string)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expr_relational()
                self.state = 183
                self.op_binary_string()
                self.state = 184
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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
        self.enterRule(localctx, 34, self.RULE_expr_relational)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.expr_logical(0)
                self.state = 190
                self.op_binary_relational()
                self.state = 191
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 199
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 200
                    self.op_binary_logical()
                    self.state = 201
                    self.expr_adding(0) 
                self.state = 207
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr_adding, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 211
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 212
                    self.op_binary_adding()
                    self.state = 213
                    self.expr_multiplying(0) 
                self.state = 219
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_multiplying, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    self.op_binary_multiplying()
                    self.state = 225
                    self.expr_not() 
                self.state = 231
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
        self.enterRule(localctx, 42, self.RULE_expr_not)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.op_unary_logical()
                self.state = 233
                self.expr_not()
                pass
            elif token in [4, 6, 29, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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
        self.enterRule(localctx, 44, self.RULE_expr_sign)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.op_unary_sign()
                self.state = 239
                self.expr_sign()
                pass
            elif token in [4, 6, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
        self.enterRule(localctx, 46, self.RULE_expr_index)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.op_unary_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.arrayValue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.stmt_func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 255
                self.expr()
                self.state = 256
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
        self.enterRule(localctx, 50, self.RULE_kw_type_explicit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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
        self.enterRule(localctx, 52, self.RULE_kw_type)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.kw_type_explicit()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
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


        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_func_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_declaration




    def stmt_declaration(self):

        localctx = ZCodeParser.Stmt_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_declaration)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.stmt_var_declaration()
                self.state = 268
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.stmt_array_declaration()
                self.state = 271
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.stmt_func_declaration()
                self.state = 274
                self.newlineLst_1()
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
        self.enterRule(localctx, 56, self.RULE_stmt_var_declaration)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.stmt_var_declaration_explicit()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.stmt_var_declaration_dynamic()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
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
        self.enterRule(localctx, 58, self.RULE_stmt_var_declaration_explicit)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.kw_type_explicit()
                self.state = 284
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 285
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.kw_type_explicit()
                self.state = 288
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
        self.enterRule(localctx, 60, self.RULE_stmt_var_declaration_dynamic)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 294
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 296
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
        self.enterRule(localctx, 62, self.RULE_stmt_var_declaration_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.KW_VAR)
            self.state = 300
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 301
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
        self.enterRule(localctx, 64, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 304
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
        self.enterRule(localctx, 66, self.RULE_stmt_array_declaration)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.kw_type_explicit()
                self.state = 307
                self.arrayId()
                self.state = 308
                self.array_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.kw_type_explicit()
                self.state = 311
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
        self.enterRule(localctx, 68, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 316
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 317
            self.arrayDim()
            self.state = 318
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
        self.enterRule(localctx, 70, self.RULE_arrayDim)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(ZCodeParser.NUMBER)
                self.state = 321
                self.match(ZCodeParser.SB_COMMA)
                self.state = 322
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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
        self.enterRule(localctx, 72, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 327
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
        self.enterRule(localctx, 74, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 330
            self.exprLst()
            self.state = 331
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
        self.enterRule(localctx, 76, self.RULE_exprLst)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.expr()
                self.state = 334
                self.match(ZCodeParser.SB_COMMA)
                self.state = 335
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_declaration




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.KW_FUNC)
            self.state = 341
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 342
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 343
            self.paramLst()
            self.state = 344
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 345
            self.newlineLst_0()
            self.state = 346
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
        self.enterRule(localctx, 80, self.RULE_paramLst)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.param()
                self.state = 349
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
        self.enterRule(localctx, 82, self.RULE_paramLstTail)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.SB_COMMA)
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
        self.enterRule(localctx, 84, self.RULE_param)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.kw_type_explicit()
                self.state = 362
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.kw_type_explicit()
                self.state = 365
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
        self.enterRule(localctx, 86, self.RULE_func_body)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.stmt_return()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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


    class Statement_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


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
            return ZCodeParser.RULE_statement_type




    def statement_type(self):

        localctx = ZCodeParser.Statement_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_statement_type)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.stmt_var_declaration()
                self.state = 375
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.stmt_array_declaration()
                self.state = 378
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.stmt_assignment()
                self.state = 381
                self.newlineLst_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.stmt_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 384
                self.stmt_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.stmt_break()
                self.state = 386
                self.newlineLst_1()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
                self.stmt_continue()
                self.state = 389
                self.newlineLst_1()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
                self.stmt_return()
                self.state = 392
                self.newlineLst_1()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 394
                self.stmt_func_call()
                self.state = 395
                self.newlineLst_1()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 397
                self.stmt_block()
                self.state = 398
                self.newlineLst_1()
                pass


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

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.statement_type()
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
        self.enterRule(localctx, 92, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.assignment_lhs()
            self.state = 405
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
        self.enterRule(localctx, 94, self.RULE_assignment_lhs)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(ZCodeParser.KW_IF)
            self.state = 412
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 413
            self.expr()
            self.state = 414
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 415
            self.newlineLst_0()
            self.state = 416
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.KW_ELIF)
            self.state = 419
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 420
            self.expr()
            self.state = 421
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 422
            self.newlineLst_0()
            self.state = 423
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_else_statement)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(ZCodeParser.KW_ELSE)
                self.state = 426
                self.newlineLst_0()
                self.state = 427
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


        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.if_statement()
            self.state = 433
            self.newlineLst_0()
            self.state = 434
            self.elifLst()
            self.state = 435
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


        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_elifLst)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.elif_statement()
                self.state = 438
                self.newlineLst_0()
                self.state = 439
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

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(ZCodeParser.KW_FOR)
            self.state = 445
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 446
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 447
            self.expr()
            self.state = 448
            self.match(ZCodeParser.KW_BY)
            self.state = 449
            self.expr()
            self.state = 450
            self.newlineLst_0()
            self.state = 451
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
        self.enterRule(localctx, 108, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
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
        self.enterRule(localctx, 110, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
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
        self.enterRule(localctx, 112, self.RULE_stmt_return)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.KW_RETURN)
                self.state = 458
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
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
        self.enterRule(localctx, 114, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 463
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 464
            self.argLst()
            self.state = 465
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
        self.enterRule(localctx, 116, self.RULE_argLst)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 6, 29, 42, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.expr()
                self.state = 468
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
        self.enterRule(localctx, 118, self.RULE_argLstTail)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.SB_COMMA)
                self.state = 474
                self.expr()
                self.state = 475
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

        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 481
            self.newlineLst_1()
            self.state = 482
            self.statementLst()
            self.state = 483
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
        self.enterRule(localctx, 122, self.RULE_statementLst)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 16, 18, 21, 22, 23, 26, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.statement()
                self.state = 486
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
        self._predicates[18] = self.expr_logical_sempred
        self._predicates[19] = self.expr_adding_sempred
        self._predicates[20] = self.expr_multiplying_sempred
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
         




