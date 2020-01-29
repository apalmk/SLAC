package com.example.anjaniprasad.slac;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import com.google.firebase.FirebaseApp;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

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
import java.util.ArrayList;
import java.util.List;


public class Register extends Activity {
    EditText usern,email1;
    ProgressDialog prgDialog;
    String RegString,responseString;
    EditText passw,reenterpass,phone;
    RadioButton userbutton,adminbutton;
    FirebaseDatabase database;
    List<Teacher> teacherList;
    DatabaseReference dr,drr,drr2;
    int flaggy;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        FirebaseApp.initializeApp(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        flaggy=0;
        usern = (EditText) findViewById(R.id.username);
        teacherList= new ArrayList<>();
        database = FirebaseDatabase.getInstance();
        dr = database.getReference();
        phone= (EditText) findViewById(R.id.numenter1);
        email1 = (EditText) findViewById(R.id.email);
        passw = (EditText) findViewById(R.id.password);
        reenterpass = (EditText) findViewById(R.id.reenterpassword);
        userbutton = (RadioButton) findViewById(R.id.radioUser);
        adminbutton = (RadioButton) findViewById(R.id.radioAdmin);
        drr = FirebaseDatabase.getInstance().getReference("teacher");
        drr2=FirebaseDatabase.getInstance().getReference("student");
        prgDialog = new ProgressDialog(this);
//        dr= FirebaseDatabase.getInstance().getReference();
        prgDialog.setCancelable(false);
    }

    @Override
    protected void onStart() {
        super.onStart();
        drr.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                teacherList.clear();
                for (DataSnapshot dataSnapshot1:dataSnapshot.getChildren())
                {
                    Teacher t1=dataSnapshot1.getValue(Teacher.class);
                    String usern=t1.getName();
                    String passw=t1.getPass();
//                    Toast.makeText(getApplicationContext(), passw, Toast.LENGTH_LONG).show();
                    teacherList.add(t1);
                }

            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }

    public void regfunc(View view)
    {
        String usernamer= usern.getText().toString();
        String passwordr= passw.getText().toString();
        String email=email1.getText().toString();
        String repassr= reenterpass.getText().toString();
        String phone1 = phone.getText().toString();
        boolean adminr=adminbutton.isChecked();
        boolean userr=userbutton.isChecked();
        System.out.println("Start here");
        System.out.println(usernamer);
        for(Teacher t2: teacherList)
        {
            String usrn=t2.getName();
            System.out.println(usrn);
            if(usrn.equals(usernamer))
            {   Log.e("state","entered");
            flaggy=1;
                break;
            }

        }
        if(usernamer.equals("")||passwordr.equals("")||repassr.equals("")||email.equals("")||phone1.equals(""))
        {
            Toast.makeText(getApplicationContext(), "Field Vaccant", Toast.LENGTH_LONG).show();
//            return;
        }

        if(!adminr&&!userr)
        {
            Toast.makeText(getApplicationContext(), "Enter adimn or user", Toast.LENGTH_LONG).show();
//            return;
        }

        if(!passwordr.equals(repassr))
        {
            Toast.makeText(getApplicationContext(), "Password do not match", Toast.LENGTH_LONG).show();
//            return;
        }

        if(flaggy==1)
        {
            Toast.makeText(getApplicationContext(), "Usesrname already taken", Toast.LENGTH_LONG).show();
//            Toast.makeText(getApplicationContext(), "username taken", Toast.LENGTH_LONG).show();
            Intent starter = new Intent(Register.this,MainActivity.class);
            startActivity(starter);

        }
        else
        {

//            int flag = (adminr)? 1 : 0;
//            // Save the Data in Database
//            int val=loginDataBaseAdapter.insertEntry(usernamer,passwordr,flag,email);
//            if(val!=0) {
//                Toast.makeText(getApplicationContext(), "Account Successfully Created ", Toast.LENGTH_LONG).show();
//                Intent intentsu = new Intent(Register.this, Success.class);
//                startActivity(intentsu);
//            }
//            else
//            {
//                Toast.makeText(getApplicationContext(), "User name already exists", Toast.LENGTH_LONG).show();
//
//
//            }
//            try
//            {   RegString=usernamer+","+passwordr+","+email+","+adminr;
//                SendMessage sm= new SendMessage();
//                sm.execute();
//
//            }
//            catch(Exception e)
//            {
//                    Toast.makeText(getApplicationContext(), "There was JSON error", Toast.LENGTH_SHORT).show();
//            }
//            If adminr is false it is student else teacher
            if(adminr)
            {
                Teacher t= new Teacher(usernamer,email,passwordr,phone1);
                String s=t.getName();
                Toast.makeText(getApplicationContext(), s, Toast.LENGTH_SHORT).show();
                String id=dr.push().getKey();
                dr.child("teacher").child(id).setValue(t);
                Intent start = new Intent(Register.this,Login.class);
                startActivity(start);
//                myRef.child("s1").setValue("Hello, World!");
//                myRef.setValue("val");
            }
            else
            {

                Student s= new Student(usernamer,email,passwordr,phone1);
                String na=s.getName();
                Toast.makeText(getApplicationContext(), na, Toast.LENGTH_SHORT).show();
                String id=dr.push().getKey();
                dr.child("student").child(id).setValue(s);
                Intent start = new Intent(Register.this,Login.class);
                startActivity(start);
//                myRef.child("s1").setValue("Hello, World!");
//                myRef.setValue("val");

            }
        }


    }

//    public class SendMessage extends AsyncTask<Void, Void, Integer> {
//
//        @Override
//        protected Integer doInBackground(Void... params) {
//
//            HttpClient httpClient = new DefaultHttpClient();
//            HttpPost httpPost = new HttpPost("http://192.168.43.36:5000/register");
//
////
//            JSONObject json = new JSONObject();
//            try {
//                json.put("regdata", RegString);
//                Log.e("Trial string",RegString);
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
//                Intent myIntent = new Intent(Register.this, Login.class);
//                myIntent.putExtra("result",responseString); //Optional parameters
//                Register.this.startActivity(myIntent);
////                Toast.makeText(MainActivity.this, responseString,Toast.LENGTH_LONG).show();
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

        Intent start = new Intent(Register.this,MainActivity.class);
        startActivity(start);
        finish();
    }
}


