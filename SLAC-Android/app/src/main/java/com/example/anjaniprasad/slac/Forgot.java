package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class Forgot extends AppCompatActivity {
int s=0;
String output="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_forgot);
        SendMessage2 sm= new SendMessage2();
        sm.execute();
    }
    public void doprint(View view)
    {
        System.out.println(s);

            Toast.makeText(getApplicationContext(),"sent" , Toast.LENGTH_SHORT).show();

    }

    public class SendMessage2 extends AsyncTask<Void, Void, Integer> {

        @Override
        protected Integer doInBackground(Void... params) {
            int status=0;
            try {

                URL url = new URL("http://192.168.43.36:5000/forgot");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setRequestProperty("Accept", "application/json");

                if (conn.getResponseCode() != 200) {
                    throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                }

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));
                System.out.println("Output from Server .... \n");
                while ((output = br.readLine()) != null) {
                   System.out.println(output);
                   if(output.equalsIgnoreCase("success"))
                   {
                       status=1;
                       s=1;
                   }
                }

                conn.disconnect();

            } catch (MalformedURLException e) {

                e.printStackTrace();

            } catch (IOException e) {

                e.printStackTrace();

            }
            return 1;
        }


    }


    @Override
    public void onBackPressed() {

        Intent start = new Intent(Forgot.this,MainActivity.class);
        startActivity(start);
        finish();
    }
}
