# Predicting-House-Income-with-Decision-Trees
The Dataset that will be used for this project is known as the Census Income Dataset.
In this project, information from the Census Income Dataset is used to predict the
income of a family living in the United States using attributes such as age, occupation, fnlwgt, ect.
For catergorical attributes, I will have the following values corresponding to each
categorical attribute:

 - working-class:<br />
		Private -> 1 <br />
		Sel-emp-not-inc -> 2 <br />
		Self-emp-inc -> 3 <br />
		Federal-gov -> 4 <br />
		Local-gov -> 5<br />
		State-gov -> 6<br />
		Without-pay -> 7<br />
		Never-worked -> 8<br />
 - education:<br />
		Bachelors -> 1<br />
		Some college -> 2<br />
		11th -> 3<br />
		HS-grad -> 4<br />
		Prof-school -> 5<br />
		Assoc-acdm -> 6<br />
		Assoc-voc -> 7<br />
		9th -> 8<br />
		7th-8th -> 9<br />
		12th -> 10 <br />
		Masters -> 11<br />
		1st-4th -> 12<br />
		10th -> 13<br />
		Doctorate -> 14<br />
		5th-6th -> 15<br />
		Preschool -> 16<br />
 - marital-status:<br />
		Married-civ-spouse -> 1<br />
		Divorced -> 2<br />
		Never-married -> 3<br />
		Separated -> 4<br />
		Widowed -> 5<br />
		Married-spouse-absent -> 6<br />
		Married-AF-spouse -> 7<br />
 - occupation:<br />
		Tech-support -> 1<br />
		Craft-repair -> 2<br />
		Other-service -> 3<br />
		Sales -> 4 <br />
		Exec-managerial -> 5<br />
		Prof-specialty -> 6 <br />
		Handlers-cleaner -> 7<br />
		Machine-op-inspct -> 8<br />
		Adm-clerical -> 9<br />
		Farming-fishing -> 10<br />
		Transport-moving -> 11<br />
		Priv-house-serv -> 12<br />
		Armed-Forces -> 13 <br />
		Protective-serv ->14<br />
 - relationship:<br />
		Wife -> 1<br />
		Own-child -> 2<br />
		Husband -> 3<br />
		Not-in-family -> 4<br />
		Other-relative -> 5<br />
		Unmarried -> 6<br />
 - race:<br />
		White -> 1<br />
		Asian-Pac-Islander -> 2<br />
		Amer-Indian-Eskimo -> 3<br />
		Other -> 4<br />
		Black -> 5<br />
 - sex:<br />
		Female -> 1<br />
		Male -> 2<br />
 - native-country:<br />
		United-States -> 1<br />
		Cambodia -> 2<br />
		England -> 3<br />
		Puerto-Rico -> 4<br />
		Canada -> 5<br />
		Germany -> 6<br />
		Outlying-US(Guam-USVI-etc) -> 7<br />
		India -> 8<br />
		Japan -> 9<br />
		Greece -> 10<br />
		South -> 11<br />
		China -> 12<br />
		Cuba -> 13<br />
		Iran -> 14<br />
		Honduras -> 15<br />
		Philipines -> 16<br />
		Italy -> 17<br />
		Poland -> 18<br />
		Jamaica -> 19<br />
		Vietnam -> 20<br />
		Mexico -> 21<br />
		Portugal -> 22<br />
		Ireland -> 23<br />
		France -> 24<br />
		Dominican Republic -> 25<br />
		Laos -> 26<br />
		Ecuador -> 27<br />
		Taiwan -> 28<br />
		Haiti -> 29<br />
		Columbia -> 30<br />
		Hungary -> 31<br />
		Guatemala -> 32<br />
		Nicaragua -> 33<br />
		Scotland -> 34<br />
		Thailand -> 35<br />
		Yugoslavia -> 36<br />
		El-Salvador -> 37<br />
		Trinidad&Tobago -> 38<br />
		Peru -> 39<br />
		Hong -> 40<br />
		Holand-Netherlands -> 41<br />
 - Income:<br />
		<= 50K -> 0<br />
		>50K -> 1
		
