def standardize_capitalisation_and_spacing(df):
    for col in df.columns:
        try:
            df[col] = df[col].astype(str).str.strip().str.lower().str.capitalize()
        except Exception:
            continue


def impute_by_median(df, *cols):
    columns = list(cols)
    for column in columns:
        try:
            df[column] = df[column].fillna(df[column].median())
            print(f"Imputed missing values for column: {column}")
        except KeyError:
            print(f"Column: {column} does not exist in dataframe")
        except TypeError:
            print(
                f"Column: {column} does not belong to the numeric type and unable to compute median."
            )
        except Exception as e:
            print(f"Error: {e}")


def impute_by_mode(df, *cols):
    columns = list(cols)
    for column in columns:
        try:
            df[column] = df[column].fillna(df[column].mode()[0])
            print(f"Imputed missing values for column: {column}")
        except KeyError:
            print(f"Column: {column} does not exist in dataframe")
        except Exception as e:
            print(f"Error: {e}")
