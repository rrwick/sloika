import numpy as np
import unittest

from sloika import decode


class TestDecode(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.post = [[0.144983872, 0.0353539565, 0.460170397, 0.0003722599, 0.3591195148],
                     [0.100967586, 0.0357787755, 0.003763944, 0.0135964994, 0.8458931946],
                     [0.225580112, 0.0053868825, 0.127545423, 0.0438386941, 0.5976488894],
                     [0.034071887, 0.0124396516, 0.390811281, 0.0058303676, 0.5568468128],
                     [0.070028528, 0.3403599935, 0.157938013, 0.3416912224, 0.0899822435],
                     [0.010880335, 0.8579484836, 0.112103479, 0.0185191681, 0.0005485341],
                     [0.009025176, 0.8074192531, 0.039663213, 0.0830854627, 0.0608068949],
                     [0.141001418, 0.3820869847, 0.179637615, 0.2329239763, 0.0643500054],
                     [0.226134609, 0.2082560019, 0.481295410, 0.0826148125, 0.0016991672],
                     [0.048037662, 0.0004689463, 0.354844142, 0.0071289458, 0.5895203039]]

        self.post3 = [[6.93038553e-02, 8.36311738e-05, 6.14328455e-05, 3.21552652e-05,
                       3.02682092e-05, 4.65413206e-04, 5.12956867e-05, 8.16535103e-05,
                       1.85443918e-04, 3.82840990e-05, 1.00521007e-04, 9.08780930e-06,
                       3.77532269e-05, 3.97826734e-05, 2.35787738e-05, 6.50650327e-05,
                       6.45387126e-06, 3.78188514e-03, 2.55392794e-03, 1.69650232e-03,
                       3.61763500e-03, 4.58211638e-03, 1.11442257e-03, 2.58183177e-03,
                       3.30588259e-02, 3.18421575e-04, 3.21677024e-03, 3.28214897e-04,
                       3.80738522e-04, 1.36162539e-03, 2.62334015e-05, 8.58768763e-04,
                       8.54791579e-05, 2.74593513e-05, 1.57945560e-05, 1.62333417e-05,
                       2.73790101e-06, 2.19068010e-04, 2.30974401e-05, 1.97779664e-05,
                       1.89241735e-04, 3.50109258e-05, 8.43457965e-05, 2.90771604e-05,
                       1.90537248e-05, 2.16106200e-05, 5.43656051e-06, 2.87465991e-05,
                       1.11084928e-05, 2.88579706e-02, 2.48598129e-01, 2.20043771e-02,
                       8.56508613e-02, 7.70513760e-03, 5.78329386e-03, 1.08525215e-03,
                       5.44386357e-02, 7.41035165e-03, 2.96513677e-01, 1.47058070e-02,
                       2.52563544e-02, 1.73825417e-02, 1.70952305e-02, 8.05289112e-03,
                       2.85326056e-02],
                      [4.18020114e-02, 2.18149461e-03, 4.18256409e-02, 1.51041220e-03,
                       3.83024174e-03, 1.13335215e-02, 2.75135133e-02, 5.27970819e-03,
                       2.94830292e-01, 6.24091714e-04, 2.48417649e-02, 5.30844321e-04,
                       5.32948703e-04, 2.66299080e-02, 1.91247452e-03, 1.50251277e-02,
                       1.74542200e-02, 6.95439530e-06, 1.77256938e-03, 5.45414969e-06,
                       1.26436492e-03, 6.27363916e-05, 1.30362780e-04, 1.57003797e-05,
                       1.12359168e-03, 4.56490307e-06, 1.69395772e-03, 4.74140052e-06,
                       2.69176002e-04, 3.65384185e-04, 1.04762882e-03, 1.36631925e-03,
                       1.32573783e-01, 1.06922910e-03, 1.61468796e-03, 7.94189633e-04,
                       2.38729859e-04, 3.79558094e-02, 4.47402820e-02, 7.60454917e-03,
                       1.95714802e-01, 2.15748005e-04, 2.45186221e-02, 2.65106966e-04,
                       1.00895137e-04, 7.45138386e-03, 1.25953066e-03, 3.74608627e-03,
                       2.11164844e-03, 2.24502946e-06, 2.67354553e-05, 1.57691295e-06,
                       3.36685553e-05, 3.54910321e-06, 2.86682302e-06, 9.22902416e-07,
                       7.00705459e-06, 4.10729808e-06, 1.30384842e-05, 1.94793142e-06,
                       1.17244626e-05, 2.29236612e-05, 7.19989301e-04, 4.60332412e-05,
                       1.03348428e-02],
                      [4.16737229e-01, 3.73092247e-04, 3.21942178e-04, 2.07630379e-04,
                       5.48811367e-05, 1.76292788e-02, 5.66177741e-02, 6.67140447e-03,
                       1.11582577e-01, 2.51698395e-04, 9.00109007e-04, 1.40585777e-04,
                       2.42681544e-05, 2.97163054e-03, 8.14701707e-05, 2.53339694e-03,
                       1.66042219e-03, 2.78048333e-06, 1.19763557e-04, 1.81204746e-06,
                       7.92458159e-05, 2.67018950e-05, 4.45836376e-05, 8.39072982e-06,
                       2.53880717e-05, 8.73791407e-07, 6.68762295e-05, 1.65151744e-06,
                       3.04315672e-05, 6.84462197e-04, 8.39502027e-04, 2.16872571e-03,
                       1.85998201e-01, 1.58521852e-05, 7.28148780e-06, 5.20146295e-06,
                       2.91604556e-06, 6.43351004e-02, 5.51776327e-02, 9.17739514e-03,
                       5.94518036e-02, 1.41548544e-05, 2.49227014e-05, 7.06619448e-06,
                       1.22111237e-06, 7.90824415e-04, 2.65337221e-05, 1.67621067e-04,
                       1.23669364e-04, 6.56190650e-07, 3.11625445e-06, 5.25497001e-07,
                       3.03158026e-06, 1.36964381e-05, 8.73886893e-06, 4.14995884e-06,
                       1.22367292e-05, 9.68970539e-07, 1.89208049e-06, 4.43298433e-07,
                       3.60218542e-06, 3.36106132e-05, 8.34592269e-04, 2.51473430e-05,
                       8.65616836e-04],
                      [1.94161218e-02, 3.45219101e-04, 1.86964621e-06, 4.09588538e-05,
                       3.21622019e-06, 1.36460515e-03, 1.84196586e-04, 2.78075371e-04,
                       7.57896400e-04, 8.15450912e-05, 4.58808563e-06, 5.38986524e-06,
                       2.35547964e-06, 8.81874530e-06, 5.69473241e-06, 4.13225735e-06,
                       1.20136906e-06, 2.02256963e-02, 1.15355261e-01, 6.68785581e-03,
                       2.26657838e-02, 5.85966185e-02, 2.30232440e-02, 2.30290759e-02,
                       1.54902861e-01, 1.83353398e-03, 2.58224867e-02, 2.40023411e-03,
                       1.29493582e-03, 7.46505037e-02, 2.57770298e-03, 4.02322151e-02,
                       1.77264831e-03, 1.67427315e-05, 5.18527827e-07, 3.97150916e-06,
                       1.04234402e-06, 4.03273239e-04, 4.00211829e-05, 4.96177672e-05,
                       1.11434369e-04, 7.42995326e-06, 6.19071216e-06, 4.13769521e-06,
                       1.38670532e-06, 1.39758401e-06, 1.63437460e-06, 3.91470337e-07,
                       1.57938666e-06, 1.92253257e-03, 2.39047855e-02, 2.94920197e-03,
                       2.99876370e-03, 4.04748553e-03, 6.96312729e-03, 7.81683193e-04,
                       2.45640520e-03, 2.72433204e-03, 2.40125638e-02, 2.33157608e-03,
                       1.60532002e-03, 6.34607002e-02, 5.33042625e-02, 4.32590470e-02,
                       1.65050894e-01],
                      [6.80756092e-01, 3.13296943e-04, 8.96118654e-05, 8.22118527e-05,
                       7.94680363e-06, 1.79889351e-02, 6.90987241e-03, 1.67462765e-03,
                       1.41790963e-03, 8.52476151e-05, 4.01970246e-05, 2.07853809e-05,
                       2.48552283e-06, 2.17500230e-04, 4.82568748e-06, 1.13193302e-04,
                       1.87015990e-04, 7.57693360e-03, 2.25060154e-03, 3.59616964e-03,
                       3.58104939e-04, 8.82236660e-03, 2.97280913e-03, 3.15465522e-03,
                       8.96902347e-04, 2.77978048e-04, 5.61335124e-04, 2.78492284e-04,
                       5.61880042e-05, 5.25417738e-03, 7.76441520e-05, 3.81301809e-03,
                       1.32718449e-03, 3.88170956e-05, 7.17060466e-05, 1.92290918e-05,
                       3.08021572e-06, 2.54950556e-03, 2.90744385e-04, 1.91270839e-04,
                       2.35827611e-04, 5.05641183e-05, 1.21982375e-04, 3.72419563e-05,
                       3.54526583e-06, 4.69271399e-05, 6.94696291e-06, 2.88536248e-05,
                       1.43770390e-04, 1.56540219e-02, 2.67669465e-02, 1.09104924e-02,
                       7.19311088e-03, 1.48529001e-02, 3.53274331e-03, 1.09531113e-03,
                       3.50503880e-03, 7.37120165e-03, 1.88682862e-02, 1.06875887e-02,
                       6.76238211e-03, 5.52225709e-02, 3.70934270e-02, 1.61395166e-02,
                       9.31814685e-03],
                      [6.34862661e-01, 1.58092575e-04, 1.04013889e-04, 6.13113953e-05,
                       4.59116163e-05, 2.04483327e-03, 1.70931016e-04, 2.52738100e-04,
                       2.62225716e-04, 4.31401313e-05, 7.41454860e-05, 2.03652107e-05,
                       3.00197171e-05, 4.06380605e-05, 8.44735860e-06, 3.62060964e-05,
                       1.48330146e-05, 1.32156508e-02, 5.23894327e-03, 8.53997190e-03,
                       1.66933110e-03, 3.45789385e-03, 5.51441160e-04, 1.42363948e-03,
                       6.57853391e-03, 5.52870275e-04, 2.62696901e-03, 6.33501448e-04,
                       1.36696559e-04, 5.11054765e-04, 1.55913513e-05, 1.00350613e-03,
                       1.18524040e-04, 2.15327527e-05, 1.91723866e-05, 1.41578785e-05,
                       5.78353001e-06, 6.19533879e-04, 2.12537161e-05, 1.09954373e-04,
                       1.60605923e-04, 4.34472349e-05, 1.10848989e-04, 3.94833987e-05,
                       2.72586040e-05, 1.20154182e-05, 8.55518556e-06, 1.77216698e-05,
                       1.02826561e-05, 2.91879755e-02, 1.01488933e-01, 1.14377933e-02,
                       3.80307958e-02, 3.55633209e-03, 9.56496224e-04, 4.13562928e-04,
                       2.19107829e-02, 4.76268446e-03, 8.10406134e-02, 8.07256158e-03,
                       9.73338075e-03, 1.15613209e-03, 3.37114296e-04, 9.29840258e-04,
                       1.23876589e-03],
                      [3.30804884e-02, 1.15964040e-02, 9.73711815e-03, 4.07537911e-03,
                       1.47854316e-03, 8.99300203e-02, 6.24509603e-02, 3.46397944e-02,
                       2.12573737e-01, 1.99409272e-03, 7.64068030e-03, 8.05901829e-04,
                       1.42606418e-03, 4.85788705e-03, 3.48505710e-04, 2.91125500e-03,
                       1.11314999e-02, 1.23465288e-04, 3.80684547e-02, 9.93413996e-05,
                       5.30149229e-03, 1.11473177e-03, 4.52168286e-03, 5.18159650e-04,
                       2.89105345e-03, 1.05692619e-04, 9.12134536e-03, 1.03393722e-04,
                       1.93851511e-03, 9.73264594e-03, 1.66891608e-03, 1.72822550e-02,
                       7.60684311e-02, 1.63225946e-03, 2.17540990e-04, 5.71767916e-04,
                       7.47620361e-05, 1.01679862e-01, 2.82327384e-02, 1.30412066e-02,
                       6.42715618e-02, 5.42319438e-04, 5.79573493e-03, 8.56171886e-04,
                       7.71885214e-04, 3.89958569e-03, 4.82406642e-04, 2.12683016e-03,
                       3.64291272e-03, 3.06215661e-05, 6.23798231e-04, 3.70811504e-05,
                       1.49028376e-04, 7.74471046e-05, 5.83706205e-05, 1.84609762e-05,
                       1.36388053e-05, 9.89449545e-05, 2.16005923e-04, 5.46358715e-05,
                       4.73836189e-05, 7.32624379e-04, 8.10936652e-03, 1.90924038e-03,
                       1.00645885e-01],
                      [5.86129367e-01, 1.24000106e-03, 1.19599674e-04, 2.15520893e-04,
                       3.20935942e-05, 2.03912482e-02, 5.65457996e-03, 4.28980496e-03,
                       9.55087692e-03, 1.49222979e-04, 1.35144859e-04, 2.79663818e-05,
                       1.49015978e-05, 1.71312582e-04, 8.34730417e-06, 9.50330723e-05,
                       1.40277494e-04, 2.14891115e-04, 4.50551659e-02, 2.99084466e-04,
                       5.71864890e-03, 1.32946705e-03, 2.92823417e-03, 6.68790133e-04,
                       4.24172962e-03, 1.78034985e-04, 8.01786594e-03, 2.10780781e-04,
                       1.09992828e-03, 1.72466300e-02, 1.32644793e-03, 4.59040962e-02,
                       2.34826207e-02, 2.64060182e-05, 1.19303768e-05, 1.04305991e-05,
                       2.99123667e-06, 9.82374139e-03, 7.24343059e-04, 5.27328753e-04,
                       1.41209469e-03, 1.25948982e-05, 6.14728779e-05, 8.89077091e-06,
                       9.05698289e-06, 6.80956873e-05, 5.34334504e-06, 2.24796368e-05,
                       8.29595447e-05, 4.62981989e-05, 5.68147749e-04, 7.41501644e-05,
                       1.27761145e-04, 1.17587006e-04, 8.65821712e-05, 2.95409791e-05,
                       4.04590246e-05, 1.60140218e-04, 5.26982127e-04, 1.11449182e-04,
                       1.11559348e-04, 2.43557314e-03, 2.30411123e-02, 6.88982802e-03,
                       1.66534975e-01],
                      [2.64359653e-01, 1.67475571e-03, 1.47722330e-05, 2.43650880e-04,
                       1.04934088e-05, 2.16121343e-03, 2.13120482e-04, 8.04431445e-04,
                       3.76285840e-04, 1.68005950e-04, 2.08266865e-05, 1.88407503e-05,
                       1.05736526e-05, 8.22252696e-06, 1.70675980e-06, 6.24488439e-06,
                       2.86770728e-06, 2.16403902e-02, 9.66359526e-02, 8.76140129e-03,
                       5.67835085e-02, 1.85416415e-02, 3.44535871e-03, 1.80904083e-02,
                       6.94842860e-02, 1.12517586e-03, 4.25357819e-02, 2.23815860e-03,
                       3.90590518e-03, 3.66540253e-03, 9.33413976e-05, 6.87892502e-03,
                       5.30657999e-04, 4.04094062e-05, 2.01770308e-06, 1.20722443e-05,
                       1.73895103e-06, 9.65902524e-04, 3.76462449e-05, 1.39234209e-04,
                       7.17739604e-05, 2.87861149e-05, 3.39707403e-05, 2.76046394e-05,
                       3.12888369e-05, 4.30486489e-06, 1.36237850e-06, 2.97293695e-06,
                       5.11134385e-06, 6.31124061e-03, 8.79523382e-02, 5.72398072e-03,
                       8.79544392e-03, 8.62585474e-03, 8.55658110e-03, 1.82847120e-03,
                       1.20783597e-02, 2.82878499e-03, 1.43523827e-01, 7.14860298e-03,
                       8.40650313e-03, 1.22847641e-02, 6.47594966e-03, 1.86637864e-02,
                       3.49373631e-02],
                      [4.31578249e-01, 1.70997251e-03, 7.09119195e-04, 6.34574622e-04,
                       9.85594306e-05, 9.30772573e-02, 4.72702645e-02, 4.25975174e-02,
                       4.54116166e-02, 3.36446974e-04, 6.66626787e-04, 1.49528918e-04,
                       4.06902145e-05, 1.29592675e-03, 2.20648344e-05, 1.08295202e-03,
                       5.76902530e-04, 4.26759128e-04, 3.88442613e-02, 4.25731676e-04,
                       6.25370443e-03, 1.84572442e-03, 2.31458130e-03, 1.10529538e-03,
                       3.26064508e-03, 1.58121795e-04, 1.00197541e-02, 2.76274717e-04,
                       1.16063247e-03, 2.11627479e-03, 1.62434982e-04, 5.64885931e-03,
                       5.58333844e-03, 1.27010455e-04, 4.67632271e-05, 6.37493067e-05,
                       1.31299948e-05, 3.32179442e-02, 3.28222057e-03, 4.24823817e-03,
                       3.95076303e-03, 1.29722568e-04, 7.31731649e-04, 9.47556618e-05,
                       2.97701081e-05, 3.01137479e-04, 2.22461440e-05, 3.18125240e-04,
                       3.10995121e-04, 1.41135853e-04, 4.62442636e-03, 2.87229574e-04,
                       1.02373993e-03, 1.46430582e-04, 8.55838734e-05, 3.18884740e-05,
                       6.92826943e-05, 5.70784207e-04, 3.29428283e-03, 4.84669639e-04,
                       7.35091045e-04, 2.85416329e-03, 8.81061517e-03, 7.40408199e-03,
                       1.75687626e-01]]

        self.post = np.array(self.post)
        self.post3 = np.array(self.post3)
        self.labels = np.array([2, 4, 4, 4, 3, 1, 1, 1, 2, 4])
        self.bases = np.array([2, 3, 1, 1, 1, 2])
        self.score = -4.4275354890527474
        self.score_full = -5.0702616325672301
        self.score_viterbi = -5.70653594347

    def test_001_argmax(self):
        bases = decode.argmax(self.post, zero_is_blank=False)
        self.assertEqual(len(bases), len(self.bases))
        self.assertTrue(np.array_equiv(bases, self.bases))

    def test_002_score(self):
        score = decode.score(self.post, self.bases)
        self.assertAlmostEqual(score, self.score)

    def test_003_score_full_length(self):
        score = decode.score(self.post, self.bases, full=True)
        self.assertAlmostEqual(score, self.score_full)

    def test_004_score_ordering(self):
        bases = decode.argmax(self.post, zero_is_blank=False)
        score1 = decode.score(self.post, bases)
        score2 = decode.score(self.post, bases, full=True)
        vpath = np.argmax(self.post, axis=1)
        vscore = np.sum(np.log([p[vp] for p, vp in zip(self.post, vpath)]))

        self.assertGreaterEqual(score1, score2)
        self.assertGreaterEqual(score2, vscore)

    def test_005_transposed_score(self):
        score = decode.forwards_transpose(self.post, self.bases)
        self.assertAlmostEqual(score, self.score_full)

        bases = decode.argmax(self.post)
        scoreF = decode.forwards_transpose(self.post, bases)
        scoreB = decode.backwards_transpose(self.post, bases)
        self.assertAlmostEqual(scoreF, scoreB)

    def test_007_viterbi(self):
        score, path = decode.viterbi(self.post3, 3)
        self.assertAlmostEqual(score, -11.130084569094556)
        self.assertEqual(path, [49, 7, 63, 63])

    def test_008_viterbi_with_skippen(self):
        score, path = decode.viterbi(self.post3, 3, skip_pen=3.0)
        self.assertAlmostEqual(score, -11.936803444063674)
        self.assertEqual(path, [49, 7, 31, 63, 63])


class TestDecodeModifiedBases(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bases = "AGGTCOGGTOOCC"
        self.seq = [13, 64, 0, 67, 85, 0, 48, 0, 0, 113, 64, 0, 100, 0, 0, 122, 0, 107]
        post = np.ones((len(self.seq), 126)) * 0.001
        post[range(len(self.seq)), self.seq] = 1
        self.post = post / post.sum(1, keepdims=True)

    def test_viterbi(self):
        score, path = decode.viterbi(self.post, 3, skip_pen=5.0, nbase=5)
        self.assertEqual(path, [x - 1 for x in self.seq if x])
