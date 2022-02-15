
import re, pyperclip

example = '''
Vollara # 101543
Final label copy # 000K5190000
Quote # 78762
Rev to H581 (several rinky-dink changes – see Zoho)				02/05/22
Capsule size: #0 clear vegetarian
Please refer to the VQ Label Review Checklist as a guideline for an acceptable label layout.

This Supplement Facts has been updated to comply with the new FDA regulations, “Food Labeling: Revision of the Nutrition and Supplement Facts Labels”, which took effect on July 26, 2016.

EFL Sport Re:Fuel
Dietary Supplement

	Supplement Facts
	Serving Size: 2 Capsules
Servings Per Container: Please complete
		Amount Per Serving	% Daily Value
	Vitamin A (100% as natural beta-carotene)	162 mcg	18%
	Vitamin C	20 mg	22%
	Vitamin D [as (D3) cholecalciferol] 	20 mcg (800 IU)	100%
	Vitamin E (as natural mixed tocopherols with tocotrienols)	6.7 mg	45%
	Thiamin (as thiamin HCl)	0.5
		Riboflavin	0.56 mg	43%
	Niacin (as niacinamide)	6.6 mg	41%
	Vitamin B6 (as pyridoxal-5-phosphate)	0.66 mg	39%
	Folate (as calcium L-5-methyltetrahydrofolate)	222 mcg DFE	56%
	Vitamin B12 (as methylcobalamin)	2 mcg	83%
	Biotin 	100 mcg	333%
	Pantothenic acid (as D-calcium pantothenate)	3.3 mg	66%
	Calcium 	50 mg	4%
	Iron (as Ferrochel® ferrous bisglycinate chelate)	0.76 mg	4%
	Iodine (as potassium iodide)	50 mcg	33%
	Magnesium 	25 mg	6%
	Zinc 	3 mg	27%
	Selenium (as Albion® selenium glycinate complex)	5 mcg	9%
	Copper 	0.4 mg	44%
	Manganese 	0.26 mg	11%
	Chromium (as TRAACS® chromium nicotinate glycinate chelate)	70 mcg	200%
	Molybdenum (as molybdenum amino acid chelate)	5 mcg	11%
	Essentials for Life:
TRAACS® calcium bisglycinate chelate buffered with calcium carbonate, TRAACS® magnesium bisglycinate chelate buffered with magnesium oxide, TRAACS® zinc bisglycinate chelate, TRAACS® magnesium glycinate glutamine chelate, TRAACS® copper bisglycinate chelate, TRAACS® manganese bisglycinate chelate, vanadium amino acid chelate, Bororganic® boron glycine complex	369 mg	*
	Proprietary Whole Food Vitamin and Antioxidant Blend:
Acerola fruit extract, garlic, kelp, rutin, broccoli, brussels sprouts, cabbage, spinach leaf, beet root, pomegranate fruit extract, chlorella algae, cranberry extract, Jerusalem artichoke root inulin, quercetin dihydrate, alfalfa leaf, blueberry fruit, carrot root, ginger root, grape seed extract, green pepper fruit, olive leaf extract, raspberry juice powder, shiitake mushroom extract, spirulina, sweet potato tuber, turmeric root extract, olive fruit extract, pine bark extract, resveratrol (from Polygonum cuspidatum root extract)	265 mg	*
	Proprietary Digestive Enzyme Blend:
Acid protease, fungal protease, glucoamylase, invertase, malt diastase, lactase, cellulase, lipase, fungal amylase, peptidase 	140 mg	*
	Proprietary Probiotic Blend: (2 billion CFU)†
Lactobacillus acidophilus, Bifidobacterium lactis, Streptococcus thermophilus, Bifidobacterium breve, Lactobacillus rhamnosus, Lactobacillus paracasei, Lactobacillus plantarum, Bifidobacterium bifidum, Bifidobacterium longum, Bifidobacterium adolescentis in a base of fructo-oligosaccharides from chicory root inulin	100 mg	*
	Vitamin K2 (as menaquinone-7 from soy)	20 mcg	*
	* Daily value not established.
Other ingredients: Hypromellose, vegetable stearic acid, ascorbic acid, rice flour, and silica.

'''

find_product = re.compile(r'((?<=\w{3})?(?P<product>[abdefghijkl]\d{3}))(?=\w{4})?',re.IGNORECASE|re.DOTALL)
find_name = re.compile(r'((?:2016\.\n*(?P<name>[\w \S]*))(?!Dietary Supplement))',re.IGNORECASE)
# example = pyperclip.paste()
found_product = find_product.search(example)
found_name = find_name.search(example)
# print(found_name.group(1))

print(found_product.group('product'))
print(found_name.group('name'))
print(re.findall(find_product,example))
# print(re.finditer(found_product.group(1)))
print(re.findall(found_name.group('name'),example))












