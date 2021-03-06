# -*- coding: utf-8 -*-

import system_tests


@system_tests.CopyFiles("$data_path/exiv2-empty.jpg")
class OptimizeBinaryArrayElements(metaclass=system_tests.CaseMeta):

    url = "http://dev.exiv2.org/issues/666"

    filename = "$data_path/exiv2-empty_copy.jpg"
    commands = [
        """$exiv2 -u -v -M"set Exif.Image.Make NIKON" -M"set Exif.Image.Model D90" -M"set Exif.Nikon3.ShutterCount 100" -M"set Exif.Nikon3.SerialNumber 123" -M"set Exif.NikonSi02xx.Version 48 50 51 52" -M"set Exif.NikonSi02xx.ShutterCount 100" $filename""",
        "$exiv2 -u -pa -u -b $filename"
    ]
    stdout = [
        """File 1/1: $filename
Set Exif.Image.Make "NIKON" (Ascii)
Set Exif.Image.Model "D90" (Ascii)
Set Exif.Nikon3.ShutterCount "100" (Long)
Set Exif.Nikon3.SerialNumber "123" (Ascii)
Set Exif.NikonSi02xx.Version "48 50 51 52" (Byte)
Set Exif.NikonSi02xx.ShutterCount "100" (Long)
""",
        """Exif.Image.Make                              Ascii       6  NIKON
Exif.Image.Model                             Ascii       4  D90
Exif.Image.ExifTag                           Long        1  56
Exif.Photo.MakerNote                         Undefined 694  78 105 107 111 110 0 2 16 0 0 73 73 42 0 8 0 0 0 3 0 167 0 4 0 1 0 0 0 100 0 0 0 29 0 2 0 4 0 0 0 49 50 51 0 145 0 7 0 122 2 0 0 50 0 0 0 0 0 0 0 48 50 51 52 21 164 34 143 235 54 112 153 177 184 174 147 103 42 220 125 13 140 250 87 163 222 8 33 41 32 6 219 159 82 244 133 5 116 210 31 91 134 160 169 161 136 94 35 215 122 12 141 253 92 170 231 19 46 56 49 25 240 182 107 15 162 36 149 245 68 130 175 203 214 208 185 145 88 14 179 71 202 60 157 237 44 90 119 131 126 104 65 9 192 102 251 127 242 84 165 229 20 50 63 59 38 0 201 129 40 190 67 183 26 108 173 221 252 10 7 243 206 152 81 249 144 22 139 239 66 132 181 213 228 226 207 171 118 48 217 113 248 110 211 39 106 156 189 205 204 186 151 99 30 200 97 233 96 198 27 95 146 180 197 197 180 146 95 27 198 96 233 97 200 30 99 151 186 204 205 189 156 106 39 211 110 248 113 217 48 118 171 207 226 228 213 181 132 66 239 139 22 144 249 81 152 206 243 7 10 252 221 173 108 26 183 67 190 40 129 201 0 38 59 63 50 20 229 165 84 242 127 251 102 192 9 65 104 126 131 119 90 44 237 157 60 202 71 179 14 88 145 185 208 214 203 175 130 68 245 149 36 162 15 107 182 240 25 49 56 46 19 231 170 92 253 141 12 122 215 35 94 136 161 169 160 134 91 31 210 116 5 133 244 82 159 219 6 32 41 33 8 222 163 87 250 140 13 125 220 42 103 147 174 184 177 153 112 54 235 143 34 164 21 117 196 2 47 75 86 80 57 17 216 142 51 199 74 188 29 109 172 218 247 3 254 232 193 137 64 230 123 255 114 212 37 101 148 178 191 187 166 128 73 1 168 62 195 55 154 236 45 93 124 138 135 115 78 24 209 121 16 150 11 111 194 4 53 85 100 98 79 43 246 176 89 241 120 238 83 167 234 28 61 77 76 58 23 227 158 72 225 105 224 70 155 223 18 52 69 69 52 18 223 155 70 224 105 225 72 158 227 23 58 76 77 61 28 234 167 83 238 120 241 89 176 246 43 79 98 100 85 53 4 194 111 11 150 16 121 209 24 78 115 135 138 124 93 45 236 154 55 195 62 168 1 73 128 166 187 191 178 148 101 37 212 114 255 123 230 64 137 193 232 254 3 247 218 172 109 29 188 74 199 51 142 216 17 57 80 86 75 47 2 196 117 21 164 34 143 235 54 112 153 177 184 174 147 103 42 220 125 13 140 250 87 163 222 8 33 41 32 6 219 159 82 244 133 5 116 210 31 91 134 160 169 161 136 94 35 215 122 12 141 253 92 170 231 19 46 56 49 25 240 182 107 15 162 36 149 245 68 130 175 203 214 208 185 145 88 14 179 71 202 60 157 237 44 90 119 131 126 104 65 9 192 102 251 127 242 84 165 229 20 50 63 59 38 0 201 129 40 190 67 183 26 108 173 221 252 10 7 243 170
Exif.MakerNote.Offset                        Long        1  74
Exif.MakerNote.ByteOrder                     Ascii       3  II
Exif.Nikon3.ShutterCount                     Long        1  100
Exif.Nikon3.SerialNumber                     Ascii       4  123
Exif.NikonSi02xx.Version                     Undefined   4  2.34
Exif.NikonSi02xx.0x0004                      Byte      102  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.ShutterCount1               Long        1  0
Exif.NikonSi02xx.DeletedImageCount           Long        1  0
Exif.NikonSi02xx.0x0072                      Byte        3  0 0 0
Exif.NikonSi02xx.VibrationReduction          Byte        1  Off
Exif.NikonSi02xx.0x0076                      Byte       12  0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.VibrationReduction1         Byte        1  Off
Exif.NikonSi02xx.0x0083                      Byte      212  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.ShutterCount2               Undefined   2  0 0
Exif.NikonSi02xx.0x0159                      Byte       85  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.VibrationReduction2         Byte        1  n/a
Exif.NikonSi02xx.0x01af                      Byte      167  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.ISO                         Byte        1  3
Exif.NikonSi02xx.0x0257                      Byte       31  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Exif.NikonSi02xx.ShutterCount                Long        1  100
"""
    ]
    stderr = [""] * 2
    retval = [0] * 2
