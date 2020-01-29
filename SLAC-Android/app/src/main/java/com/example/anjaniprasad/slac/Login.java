package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

public class Login extends AppCompatActivity {
String regString,responseString;
    RadioButton teacher,student;
    ArrayList<Teacher> returnValues = new ArrayList<Teacher>();
    DatabaseReference cr;
    FirebaseDatabase db;
    EditText id,password;
    DatabaseReference ddr;
    String username,pass;
    boolean studentt,teacherr;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);


        Button b1= (Button) findViewById(R.id.loginButton);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                id= (EditText)findViewById(R.id.username1);
                password= (EditText)findViewById(R.id.password2);
                teacher = (RadioButton) findViewById(R.id.teach1);
                student = (RadioButton) findViewById(R.id.stud1);
                username= id.getText().toString();
                pass= password.getText().toString();
                teacherr=teacher.isChecked();
                studentt=student.isChecked();
                System.out.println("After this");
                System.out.println(teacherr);
//                Toast.makeText(getApplicationContext(), teacherr, Toast.LENGTH_LONG).show();
                if ((username != null && username.length()>0)
                        && (pass != null && pass.length()>0)) {
                    regString=username+","+pass;
//                    SendMessage1 sm= new SendMessage1();
//                    sm.execute();

                    if(teacherr)
                    {
                        Intent start = new Intent(Login.this,Login1.class);
                        LoginDet det= new LoginDet(username,pass);
//                        start.putExtra("det",det);
                        Bundle extras = new Bundle();
                        extras.putString("username",username);
                        extras.putString("password",pass);
                        start.putExtras(extras);
                        startActivity(start);
                    }
                    if(studentt)
                    {
                        Intent start = new Intent(Login.this,Login2.class);
//                        start.putExtra("det",det);
                        Bundle extras = new Bundle();
                        extras.putString("username",username);
                        extras.putString("password",pass);
                        start.putExtras(extras);
                        startActivity(start);
                        //write for student login
                    }

                }
                else {
//                    Toast.makeText(getApplicationContext(), username, Toast.LENGTH_LONG).show();
                    Toast.makeText(getApplicationContext(), "Username & Password should not be empty.", Toast.LENGTH_LONG).show();
                }
            }
        });
    }







//    public class SendMessage1 extends AsyncTask<Void, Void, Integer> {
//
//        @Override
//        protected Integer doInBackground(Void... params) {
//
//            HttpClient httpClient = new DefaultHttpClient();
//            HttpPost httpPost = new HttpPost("http://192.168.43.36:5000/login");
//
////
//            JSONObject json = new JSONObject();
//            try {
//                json.put("login", regString);
//                Log.e("Trial string",regString);
//            }
//            catch (JSONException e)
//            {
//                Log.e("json-exception",e.getMessage());
//            }
//            try {
//                StringEntity params1 = new StringEntity(json.toString());
//                httpPost.setEntity(params1);
//            }
//            catch (UnsupportedEncodingException e)
//            {
//                Log.e("Unsupported encoding",e.getMessage());
//            }
//            httpPost.addHeader("content-type", "application/json");
//
////
//            org.apache.http.HttpResponse response;
//            int status = 0;
//            try {
//                response = httpClient.execute(httpPost);
//                status = response.getStatusLine().getStatusCode();
//                HttpEntity responseHttpEntity = response.getEntity();
//                InputStream content = responseHttpEntity.getContent();
//
//                BufferedReader buffer = new BufferedReader(new InputStreamReader(content));
//                String line;
//                responseString="";
//                while ((line = buffer.readLine()) != null) {
//                    responseString += line;
//                }
//
//            } catch (ClientProtocolException e) {
//                Log.e("Client Prot",e.getMessage());
//
//            } catch (IOException e) {
//                Log.e("IOException",e.getMessage());
//            }
//            return status;
//        }
//
//        @Override
//        protected void onPostExecute(Integer result) {
//            super.onPostExecute(result);
//            if (result == 200) {
//
//                if(responseString.equalsIgnoreCase("00"))
//                {
//                    Toast.makeText(getApplicationContext(),"wrong password",Toast.LENGTH_SHORT).show();
//                }
//                if(responseString.equalsIgnoreCase("01"))
//                {
//                    Toast.makeText(getApplicationContext(),"login is success",Toast.LENGTH_SHORT).show();
//                    Intent myIntent = new Intent(Login.this, PostLogin.class);
//                Login.this.startActivity(myIntent);
//                }
//                if(responseString.equalsIgnoreCase("10"))
//                {
//                    Toast.makeText(getApplicationContext(),"no such user present",Toast.LENGTH_SHORT).show();
//                }
////                Intent myIntent = new Intent(Register.this, Login.class);
////                myIntent.putExtra("result",responseString); //Optional parameters
////                Register.this.startActivity(myIntent);
//////                Toast.makeText(MainActivity.this, responseString,Toast.LENGTH_LONG).show();
//
//
//
//            } else {
//                Toast.makeText(getApplicationContext(), "Upload error",
//                        Toast.LENGTH_LONG).show();
//            }
//
//        }
//    }


    @Override
    public void onBackPressed() {

        Intent start = new Intent(Login.this,MainActivity.class);
        startActivity(start);
        finish();
    }
}
