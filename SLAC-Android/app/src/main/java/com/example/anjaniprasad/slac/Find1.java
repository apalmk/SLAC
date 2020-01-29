package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

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

public class Find1 extends AppCompatActivity {
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_find1);
        b1 = (Button) findViewById(R.id.button2);
    }

    public void check(View view) {
        Toast.makeText(getApplicationContext(), "Checking the image", Toast.LENGTH_LONG).show();
        SendMessage1 smm= new SendMessage1();
        smm.execute();
    }

    public void backk(View view)
    {
        Intent start = new Intent(Find1.this,PostLogin.class);
        startActivity(start);
    }

    public class SendMessage1 extends AsyncTask<Void, Void, Integer> {
        String responseString;

        @Override
        protected Integer doInBackground(Void... params) {

            HttpClient httpClient = new DefaultHttpClient();
            HttpPost httpPost = new HttpPost("http://192.168.43.36:5000/test");

//
            JSONObject json = new JSONObject();
            try {
                json.put("access", "ok");
            } catch (JSONException e) {
                Log.e("json-exception", e.getMessage());
            }
            try {
                StringEntity params1 = new StringEntity(json.toString());
                httpPost.setEntity(params1);
            } catch (UnsupportedEncodingException e) {
                Log.e("Unsupported encoding", e.getMessage());
            }
            httpPost.addHeader("content-type", "application/json");

//
            org.apache.http.HttpResponse response;
            int status = 0;
            try {
                response = httpClient.execute(httpPost);
                status = response.getStatusLine().getStatusCode();
                HttpEntity responseHttpEntity = response.getEntity();
                InputStream content = responseHttpEntity.getContent();

                BufferedReader buffer = new BufferedReader(new InputStreamReader(content));
                String line;
                responseString = "";
                while ((line = buffer.readLine()) != null) {
                    responseString += line;
                }

            } catch (ClientProtocolException e) {
                Log.e("Client Prot", e.getMessage());

            } catch (IOException e) {
                Log.e("IOException", e.getMessage());
            }
            return status;
        }

        @Override
        protected void onPostExecute(Integer result) {
            super.onPostExecute(result);
            if (result == 200) {

                Toast.makeText(getApplicationContext(), "The person is " + responseString, Toast.LENGTH_LONG).show();


            } else {
                Toast.makeText(getApplicationContext(), "Upload error",
                        Toast.LENGTH_LONG).show();
            }

        }
    }
}