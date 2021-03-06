from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)

DATABASE_FILE = "database.db"
DEFAULT_BUGGY_ID = "1"

BUGGY_RACE_SERVER_URL = "http://rhul.buggyrace.net"


#------------------------------------------------------------
# the index page
#------------------------------------------------------------
@app.route('/')
def home():
   return render_template('index.html', server_url=BUGGY_RACE_SERVER_URL)

#------------------------------------------------------------
# creating a new buggy:
#  if it's a POST request process the submitted data
#  but if it's a GET request, just show the form
#------------------------------------------------------------
@app.route('/new', methods = ['POST', 'GET'])
def create_buggy():
  if request.method == 'GET':
  
    #con = sql.connect(DATABASE_FILE)
    #con.row_factory = sql.Row
    #cur = con.cursor()
    #cur.execute("SELECT * FROM buggies")
    #record = cur.fetchone();
    
  
    return render_template("buggy-form.html", buggy = None)
  elif request.method == 'POST':
  
    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies")
    record = cur.fetchone();
    
    msg=""
    
    qty_wheels = request.form['qty_wheels']
 
    flag_color = request.form['flag_color']
    flag_color_secondary = request.form['flag_color_secondary']
    flag_pattern = request.form['flag_pattern']
 
    power_type = request.form['power_type']
    power_units = request.form['power_units']
    aux_power_type = request.form['aux_power_type']
    aux_power_units = request.form['aux_power_units']
    hamster_booster = request.form['hamster_booster']
 
    tyres = request.form['tyres']
    qty_tyres = request.form['qty_tyres']
 
    armour = request.form['armour']
    fireproof = request.form['fireproof']
    insulated = request.form['insulated']
    antibiotic = request.form['antibiotic']
 
    attack = request.form['attack']
    qty_attacks = request.form['qty_attacks']
 
    banging = request.form['banging']
    algo = request.form['algo']
    
    """RULES"""
    
    #qty_wheels must be even
    if int(qty_wheels)%2 != 0:
        msg = f"RULE VIOLATION! PLEASE ENTER AN EVEN INTEGER: Number of Wheels"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        
    #qty_tyres must be greater than qty_wheels
    if int(qty_tyres) < int(qty_wheels):
        msg = f"RULE VIOLATION! PLEASE ENTER AN INTEGER GREATER THAN", qty_wheels, ": Number of Tyres"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        
    
    #ensuring that an input is a number and not a word
    if not qty_wheels.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Wheels"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not power_units.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        #units rules validation needed
    elif not aux_power_units.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        #units rules validation needed
    elif not hamster_booster.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Hamster Booster"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not qty_tyres.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Tyres"
        return render_template("buggy-form.html", msg = msg, buggy = record)
    elif not qty_attacks.isdigit():
        msg = f"INVALID! PLEASE ENTER AN INTEGER: Number of Attacks"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        
    #non-consumable power must hace one unit per motive force (power_type)
    if power_type == "fusion" and int(power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", power_units)
    elif power_type == "thermo" and int(power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", power_units)
    elif power_type == "solar" and int(power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", power_units)
    elif power_type == "wind" and int(power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", power_units)
        
    #non-consumable power must hace one unit per motive force (aux_power_type)
    if aux_power_type == "fusion" and int(aux_power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", aux_power_units)
    elif aux_power_type == "thermo" and int(aux_power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", aux_power_units)
    elif aux_power_type == "solar" and int(aux_power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", aux_power_units)
    elif aux_power_type == "wind" and int(aux_power_units) > 1:
        msg = f"INVALID! 1 UNIT PERMITTED: Units of Auxiliary Power"
        return render_template("buggy-form.html", msg = msg, buggy = record)
        print("FIXME error message given", aux_power_units)

    """COST"""

    #power costs
    if power_type == "petrol":
        power_cost = int(power_units) * 4
    elif power_type == "fusion":
        power_cost = int(power_units) * 400
    elif power_type == "steam":
        power_cost = int(power_units) * 3
    elif power_type == "bio":
        power_cost = int(power_units) * 5
    elif power_type == "electric":
        power_cost = int(power_units) * 20
    elif power_type == "rocket":
        power_cost = int(power_units) * 16
    elif power_type == "hamster":
        power_cost = int(power_units) * 3
    elif power_type == "thermo":
        power_cost = int(power_units) * 300
    elif power_type == "solar":
        power_cost = int(power_units) * 40
    elif power_type == "wind":
        power_cost = int(power_units) * 20
        
    #aux power cost
    if aux_power_type == "petrol":
        aux_power_cost = int(aux_power_units) * 4
    elif aux_power_type == "fusion":
        aux_power_cost = int(aux_power_units) * 400
    elif aux_power_type == "steam":
        aux_power_cost = int(aux_power_units) * 3
    elif aux_power_type == "bio":
        aux_power_cost = int(aux_power_units) * 5
    elif aux_power_type == "electric":
        aux_power_cost = int(aux_power_units) * 20
    elif aux_power_type == "rocket":
        aux_power_cost = int(aux_power_units) * 16
    elif aux_power_type == "hamster":
        aux_power_cost = int(aux_power_units) * 3
    elif aux_power_type == "themo":
        power_cost = int(aux_power_units) * 300
    elif aux_power_type == "solar":
        aux_power_cost = int(aux_power_units) * 40
    elif aux_power_type == "wind":
        aux_power_cost = int(aux_power_units) * 20
        
    #hamster cost
    hamster_cost = int(hamster_booster) * 5
    
    #tyres cost
    if tyres == "knobbly":
        tyres_cost = int(qty_tyres) * 15
    elif tyres == "slick":
        tyres_cost = int(qty_tyres) * 10
    elif tyres == "steelband":
        tyres_cost = int(qty_tyres) * 20
    elif tyres == "reactive":
        tyres_cost = int(qty_tyres) * 40
    elif tyres == "maglev":
        tyres_cost = int(qty_tyres) * 50
    
    #armour
    if armour == "wood":
        armour_size = (int(qty_wheels)-4) * 10
        armour_cost = int(armour_size) * 40
    elif armour == "aluminimum":
        armour_size = (int(qty_wheels)-4) * 10
        armour_cost = int(armour_size) * 200
    elif armour == "thinsteel":
        armour_size = (int(qty_wheels)-4) * 10
        armour_cost = int(armour_size) * 100
    elif armour == "thicksteel":
        armour_size = (int(qty_wheels)-4) * 10
        armour_cost = int(armour_size) * 200
    elif armour == "titanium":
        armour_size = (int(qty_wheels)-4) * 10
        armour_cost = int(armour_size) * 290
    else:
        armour_cost = 0
    
    #attack cost
    if attack == "spike":
        attack_cost = int(qty_attacks) * 5
    elif attack == "flame":
        attack_cost = int(qty_attacks) * 20
    elif attack == "charge":
        attack_cost = int(qty_attacks) * 28
    elif attack == "biohazard":
        attack_cost = int(qty_attacks) * 30
    else:
        attack_cost = 0
        
    #fireproof cost
    if fireproof == "Yes":
        fireproof_cost = 70
    else:
        fireproof_cost = 0
    
    #insulated cost
    if insulated == "Yes":
        insulated_cost = 100
    else:
        insulated_cost = 0
    
    #antibiotic cost
    if antibiotic == "Yes":
        antibiotic_cost = 90
    else:
        antibiotic_cost = 0
    
    #banging cost
    if banging == "Yes":
        banging_cost = 42
    else:
        banging_cost = 0
        
    total_cost = int(power_cost) + int(aux_power_cost) + int(hamster_cost) + int(tyres_cost) + int(armour_cost) + int(attack_cost) + int(fireproof_cost) + int(insulated_cost) + int(antibiotic_cost) + int(banging_cost)
    try:
        qty_wheels = request.form['qty_wheels']
          
        flag_color = request.form['flag_color']
        flag_color_secondary = request.form['flag_color_secondary']
        flag_pattern = request.form['flag_pattern']
          
        power_type = request.form['power_type']
        power_units = request.form['power_units']
        aux_power_type = request.form['aux_power_type']
        aux_power_units = request.form['aux_power_units']
        hamster_booster = request.form['hamster_booster']
          
        tyres = request.form['tyres']
        qty_tyres = request.form['qty_tyres']
          
        armour = request.form['armour']
        fireproof = request.form['fireproof']
        insulated = request.form['insulated']
        antibiotic = request.form['antibiotic']
          
        attack = request.form['attack']
        qty_attacks = request.form['qty_attacks']
          
        banging = request.form['banging']
        algo = request.form['algo']
          
        buggy_id = request.form['id']
          
        msg = f"qty_wheels={qty_wheels}", "flag_color={flag_color}", "flag_color_secondary={flag_color_secondary}", "flag_pattern={flag_pattern}", "power_type={power_type}", "power_units={power_units}", "aux_power_type={aux_power_type}", "aux_power_units={aux_power_units}", "hamster_booster={hamster_booster}", "tyres={tyres}", "qty_tyres={qty_tyres}", "armour={armour}", "fireproof={fireproof}", "insulated={insulated}", "antibiotic={antibiotic}", "attack={attack}", "qty_attacks={qty_attacks}", "banging={banging}", "algo={algo}"
          
        with sql.connect(DATABASE_FILE) as con:
            cur = con.cursor()

        if buggy_id.isdigit():
            cur.execute("UPDATE buggies set qty_wheels=?, flag_color=?, flag_color_secondary=?, flag_pattern=?, power_type=?, power_units=?, aux_power_type=?, aux_power_units=?, hamster_booster=?, tyres=?, qty_tyres=?, armour=?, fireproof=?, insulated=?, antibiotic=?, attack=?, qty_attacks=?, banging=?, algo=?, total_cost=? WHERE id=?", (qty_wheels, flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost, buggy_id))
            print("FIXME i am working")
        else:
            cur.execute("INSERT INTO buggies (qty_wheels, flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (qty_wheels,  flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost))
            print("FIXME this is running!!!")
        
        con.commit()
        msg = "Record successfully saved"
    except:
        con.rollback()
        msg = "error in update operation"
    finally:
      con.close()
      return render_template("updated.html", msg = msg)

          
#------------------------------------------------------------
# rules for buggy form here
#------------------------------------------------------------
@app.route('/autofill', methods=['GET','POST'])
def autofill():
    if request.method == 'GET':
    
        return render_template('autofill-form.html', buggy=None)
        
    elif request.method == 'POST':
        
        con = sql.connect(DATABASE_FILE)
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM buggies")
        record = cur.fetchone();
           
        msg=""
           
        qty_wheels = request.form['qty_wheels']
        
        flag_color = request.form['flag_color']
        flag_color_secondary = request.form['flag_color_secondary']
        flag_pattern = request.form['flag_pattern']
        
        power_type = request.form['power_type']
        power_units = request.form['power_units']
        aux_power_type = request.form['aux_power_type']
        aux_power_units = request.form['aux_power_units']
        hamster_booster = request.form['hamster_booster']
        
        tyres = request.form['tyres']
        qty_tyres = request.form['qty_tyres']
        
        armour = request.form['armour']
        fireproof = request.form['fireproof']
        insulated = request.form['insulated']
        antibiotic = request.form['antibiotic']
        
        attack = request.form['attack']
        qty_attacks = request.form['qty_attacks']
        
        banging = request.form['banging']
        algo = request.form['algo']
        
        return render_template('autofill-form.html', msg=msg, buggy = record)
        
        msg = f"qty_wheels={qty_wheels}", "flag_color={flag_color}", "flag_color_secondary={flag_color_secondary}", "flag_pattern={flag_pattern}", "power_type={power_type}", "power_units={power_units}", "aux_power_type={aux_power_type}", "aux_power_units={aux_power_units}", "hamster_booster={hamster_booster}", "tyres={tyres}", "qty_tyres={qty_tyres}", "armour={armour}", "fireproof={fireproof}", "insulated={insulated}", "antibiotic={antibiotic}", "attack={attack}", "qty_attacks={qty_attacks}", "banging={banging}", "algo={algo}"
           
        with sql.connect(DATABASE_FILE) as con:
            cur = con.cursor()
        
        cur.execute("INSERT INTO buggies (qty_wheels, flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (qty_wheels,  flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, fireproof, insulated, antibiotic, attack, qty_attacks, banging, algo, total_cost))
        
        con.commit()
        msg = "Record successfully saved"
        
        con.close()
        
        return render_template("update.html", msg=msg)
              
#------------------------------------------------------------
# rules for buggy form here
#------------------------------------------------------------
@app.route('/rules')
def rules():
    return render_template('rules.html')

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/buggy')
def show_buggies():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies")
  records = cur.fetchall();
  return render_template("buggy.html", buggies = records)

#------------------------------------------------------------
# a page for editing the buggy
#------------------------------------------------------------
@app.route('/edit/<buggy_id>')
def edit_buggy(buggy_id):
    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies WHERE id=?", (buggy_id))
    record = cur.fetchone();
    
    return render_template("buggy-form.html", buggy = record)


#------------------------------------------------------------
# get JSON from current record
#   this is still probably right, but we won't be
#   using it because we'll be dipping diectly into the
#   database
#------------------------------------------------------------
@app.route('/json/<buggy_id>', methods=['GET'])
def summary(buggy_id):
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies WHERE id=? LIMIT 1", (buggy_id))
  return jsonify(
      {k: v for k, v in dict(zip(
        [column[0] for column in cur.description], cur.fetchone())).items()
        if (v != "" and v is not None)
      }
    )

#------------------------------------------------------------
# delete the buggy
#   don't want DELETE here, because we're anticipating
#   there always being a record to update (because the
#   student needs to change that!)
#------------------------------------------------------------
@app.route('/delete/<buggy_id>', methods = ['POST'])
def delete_buggy(buggy_id):
    #if request.method == "POST":
    try:
        msg = "deleting buggy"
        with sql.connect(DATABASE_FILE) as con:
            cur = con.cursor()
            if buggy_id.isdigit():
                cur.execute("DELETE FROM buggies WHERE id=?", (buggy_id,))
                print("FIXME i am working *big happy*")
            else:
                print("FIXME i am not working *big sad*")
        con.commit()
        msg = "Buggy deleted"
    except:
        con.rollback()
        msg = "error in delete operation"
    finally:
        con.close()
        return render_template("updated.html", msg = msg)
        
#------------------------------------------------------------
# poster for buggy here
#------------------------------------------------------------
@app.route('/poster')
def poster():
    return render_template('poster.html')


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")
