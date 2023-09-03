from flask import Flask, render_template, redirect, request, session  # added session!

app = Flask(__name__)
app.secret_key = '7a63b7ac5f8a5640035460f78fc4f8e17dd303eb4b78eeb01c3cd6e53db3b43f' # python -c 'import secrets; print(secrets.token_hex())'

@app.route("/") 
def home():
    if 'key_name' not in session:  
      print("key 'key_name' does NOT exist")
      session["key_name"] = 1 
    else:
      print('key exists!')
      session["key_name"] += 1

    if "counter" not in session:    
        session["counter"] = 0 
    
    return render_template("index.html", visits = session["key_name"], counters = session["counter"])



@app.route("/destroy_session", methods=["POST"])
def destroy_sess():
    session.clear()
    return redirect("/")


# NINJA BONUS
@app.route("/increm_session", methods=["POST"])
def increm_sess_two():
    session["counter"] += 2 
    return redirect("/")
                         
                         

# SENSEI BONUS
@app.route("/specify_increm", methods=["POST"])
def specify_increment():
    session["counter"] += (int(request.form["visits"])) 
    return redirect("/")



@app.errorhandler(404)  # we specify in parameter here the type of error, here it is 404
def page_not_found(
    error,
):  # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__ == "__main__":
    app.run(debug=True)
