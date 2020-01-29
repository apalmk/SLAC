package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

public class Sfl extends AppCompatActivity {
TextView tvs;
String name;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sfl);
        tvs= (TextView)findViewById(R.id.sfl_text);
        Intent iin= getIntent();
        Bundle b = iin.getExtras();

        if(b!=null)
        {
            String j = b.getString("sfl");
            name= b.getString("name");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tvs.setText(j);
        }
    }

    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Sfl.this, PostLogin1.class);
        myIntent.putExtra("name",name);

        Sfl.this.startActivity(myIntent);
    }
}
