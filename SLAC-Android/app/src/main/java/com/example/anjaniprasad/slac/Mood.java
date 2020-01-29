package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class Mood extends AppCompatActivity {
TextView tvv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mood);
        tvv=(TextView)findViewById(R.id.mood_text);
        Intent iin1= getIntent();
        Bundle b = iin1.getExtras();

        if(b!=null)
        {
            String j =(String) b.get("mood");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tvv.setText(j);
        }
    }
    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Mood.this, PostLogin.class);
        Mood.this.startActivity(myIntent);
    }
}
